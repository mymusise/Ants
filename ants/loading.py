from importlib import import_module
import os


def _not_cache_file(file):
    return False if "__pycache" in file or ".pyc" in file else True


def get_file_name(file):
    try:
        file_name, extension = file.split('.')
    except ValueError:
        raise ValueError(
            "Error loading object '{}': not a full path".format(file))
        return False
    except:
        return False
    return file_name, extension


def is_py_file(extension):
    return True if extension == 'py' else False


def get_class_by_path(path, NAME):
    files = os.listdir(path)
    files = filter(not_cache_file, files)
    for file in files:
        file_name, extension = get_file_name(file)
        if not is_py_file(extension):
            continue
        module_name = (path + file_name).replace('/', '.')
        module = import_module(module_name)
        return class_by_module_name(module_name, NAME)


def class_by_module_name(module_name, NAME):
    module = import_module(module_name)
    return _get_class(module, NAME)


def _get_class(module, NAME):
    _vars = dir(module)
    for _var in _vars:
        attr = getattr(module, _var)
        if not hasattr(attr, 'NAME'):
            continue
        value = getattr(attr, 'NAME')
        if value != NAME:
            continue
        return attr
