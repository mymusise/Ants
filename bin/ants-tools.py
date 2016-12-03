import os
import sys
import ants


def print_help():
    print("help is not complete yeah")


def start_project(argv):
    if len(sys.argv) <= 2:
        print("[Error:A project_name is requried]")
        return
    project_name = sys.argv[2]
    template_path = "%s/conf/project_template/" % ants.__path__[0]
    os.system("django-admin startproject --template %s %s" %
              (template_path, project_name))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print_help()
    command = sys.argv[1]
    if command == "startproject":
        start_project(sys.argv)
    else:
        print_help()
