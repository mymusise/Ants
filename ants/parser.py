from ants.utils import BaseMixin


class Rule(object):

    def __call__(self):
        pass


class Parser(BaseMixin):

    def rule_1(self, obj):
        print("rule_1")
        return 

    @property
    def rules(self):
        return []