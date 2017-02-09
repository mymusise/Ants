from django.core.management.base import BaseCommand
from importlib import import_module
from ants.loading import get_class_by_path
import os


class BaseAntCommand(BaseCommand):
    app_name = ''

    def add_arguments(self, parser):
        parser.add_argument('args', metavar='app_label', nargs='*',
                            help='Specify the app label(s) to create migrations for.')

    def handle(self, *args, **options):
        for name in args:
            cls = get_class_by_path('{}/ants/'.format(self.app_name))
            if not cls:
                continue
            obj = cls()
            print("runing the clawer in [{}]".format(file_obj.__name__))
            try:
                return obj.start()
            except:
                import traceback
                traceback.print_exc()
