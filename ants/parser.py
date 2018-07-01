from ants.utils import BaseMixin


class Rule(object):

    def __call__(self):
        pass


class Parser(BaseMixin):

    def multi_run(self, bulk_ids):
        for bulk_id in bulk_ids:
            self.multi_update(bulk_id)

    def rule_1(self, obj):
        print("rule_1")
        return 

    @property
    def rules(self):
        return []