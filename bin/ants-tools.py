import os, sys

def print_help():
    print("help is not complete yeah")

def start_project(argv):
    if len(sys.argv) <= 2:
        print("[Error:A project_name is requried]")
        return
    project_name = sys.argv[2]
    os.system("django-admin startproject %s" % project_name)
    os.system("cd %s" % project_name)
    # os.system("python manage.py startapp spiders")
    # os.system("python manage.py startapp parsers")

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print_help()
    command = sys.argv[1]
    if command == "startproject":
        start_project(sys.argv)
    else:
        print_help()