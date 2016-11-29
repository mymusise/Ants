from django.core.management.base import BaseCommand
from importlib import import_module
import os


class BaseAntCommand(BaseCommand):
    app_name = ''


    def add_arguments(self, parser):
        parser.add_argument('args', metavar='app_label', nargs='*',
                            help='Specify the app label(s) to create migrations for.')

    def not_cache_file(self, file):
        return False if "__pycache" in file or ".pyc" in file else True

    def get_file_name(self, file):
        try:
            file_name, extension = file.split('.')
        except ValueError:
            raise ValueError(
               "Error loading object '{}': not a full path".format(file))
            return False
        return file_name, extension

    def is_py_file(self, extension):
        return True if extension == 'py' else False

    def get_file_obj(self, file_name):
        return import_module('{}.ants.{}'.format(self.app_name, file_name))

    def handle(self, *args, **options):
        files = os.listdir('{}/ants/'.format(self.app_name))
        files = list(filter(self.not_cache_file, files))
        # map( ,args)
        for name in args:
            for file in files:
                file_name, extension = self.get_file_name(file)
                if not self.is_py_file(extension):
                    continue
                file_obj = self.get_file_obj(file_name)
                _vars = dir(file_obj)
                for _var in _vars:
                    attr = getattr(file_obj, _var)
                    if not hasattr(attr, 'NAME'):
                        continue
                    value = getattr(attr, 'NAME')
                    if value != name:
                        continue
                    obj = attr()
                    print("runing the clawer in [{}]".format(file_obj.__name__))
                    try:
                        return obj.start()
                    except:
                        import traceback
                        traceback.print_exc()
            print("[Ant not found]")
