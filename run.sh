#!/bin/bash

export PYTHONPATH=".:$PYTHONPATH"
export DJANGO_SETTINGS_MODULE="test_settings"

usage() {
    echo "USAGE: $0 [command]"
    echo "  test - run the ants tests"
    echo "  shell - open the Django shell"
    exit 1
}

case "$1" in
    "test" )
        shift;
        django-admin.py test ants $@;;
    "shell" )
        django-admin.py shell ;;
    * )
        usage ;;
esac
