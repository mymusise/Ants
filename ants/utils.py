from gevent import monkey
from django.db import transaction
import gevent
import time


monkey.patch_all(socket=True, dns=True, time=True, select=True,
                 thread=False, os=True, ssl=True, httplib=False, aggressive=True)


def group_list(_list, is_size=True):
    def with_size(size):
        count = int(len(_list) / size) + 1
        return [_list[i * size:(i + 1) * size] for i in range(count)]
    def with_count(count):
        return [_list[i::count] for i in range(count)]
    return with_size if is_size else with_count


class BaseMixin(object):
    task_model = ''
    task_model_key = 'id'
    goal_model = ''
    goal_model_key = 'id'
    related_key = ''
    container_size = 1000
    thread = 1

    def __init__(self):
        if not self.related_key:
            self.related_key = self.task_model_key

    @property
    def done_task(self):
        if not self.goal_model:
            return {}
        ids = self.goal_model.objects.all().values_list(self.related_key)
        return {"%s__in" % self.related_key: ids}

    @property
    def all_task_obj(self):
        return self.task_model.objects.filter(**self.task_obj_filter())

    @property
    def task_ids(self):
        objs = self.all_task_obj.exclude(**self.done_task)
        ids = objs.values_list(self.task_model_key)
        return list(map(lambda x: x[0], ids))

    def task_obj_filter(self):
        return {}

    def task_filter(self, task):
        return True

    def run(self, task):
        pass

    def multi_update(self, bulk_id):
        objs = self.task_model.objects.filter(
            **{"%s__in" % self.task_model_key: bulk_id})
        objs = filter(self.task_filter, objs)
        list(map(self.run, objs))

    @transaction.atomic
    def multi_run(self, bulk_ids):
        for bulk_id in bulk_ids:
            self.multi_update(bulk_id)

    def run_all(self):
        start_time = time.time()
        bulk_ids = group_list(self.task_ids)(self.container_size)
        bulk_id_group = group_list(bulk_ids, False)(self.thread)
        jobs = [gevent.spawn(self.multi_run, id_group)
                for id_group in bulk_id_group]
        gevent.joinall(jobs)
        end_time = time.time()
        print("using %s(s)" % (end_time - start_time))

    def start(self):
        self.run_all()
