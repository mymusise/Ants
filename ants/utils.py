from functional import seq
from gevent import monkey
from django.db import transaction
import gevent
import time


monkey.patch_all(socket=True, dns=True, time=True, select=True,
                 thread=False, os=True, ssl=True, httplib=False, aggressive=True)


class BaseMixin(object):
    model = ''
    model_key = ''
    container_size = 1000
    thread = 2

    def start(self):
        self.run_all()

    def get_obj(self, _id):
        return self.model.objects.get(**{self.model_key: _id})

    def get_objects_id(self):
        ids = self.model.objects.all().values_list(self.model_key)
        return seq(ids).map(lambda x: x[0])

    def obj_filter(self, obj):
        return True

    def run(self, obj):
        pass

    def multi_update(self, bulk_id):
        objs = self.model.objects.filter(
            **{"%s__in" % self.model_key: bulk_id})
        objs = filter(self.obj_filter, objs)
        list(map(self.run, objs))

    @transaction.atomic
    def multi_run(self, bulk_ids):
        for bulk_id in bulk_ids:
            self.multi_update(bulk_id)

    def run_all(self):
        start_time = time.time()
        ids = self.get_objects_id()
        bulk_ids = seq(ids).grouped(self.container_size)
        bulk_ids = list(map(list, bulk_ids))
        bulk_id_group = seq(bulk_ids).grouped(self.thread)
        bulk_id_group = list(map(list, bulk_id_group))
        jobs = [gevent.spawn(self.multi_run, id_group)
                for id_group in bulk_id_group]
        gevent.joinall(jobs)
        end_time = time.time()
        print("using %s(s)" % (end_time - start_time))
