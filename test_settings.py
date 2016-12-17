SECRET_KEY = 'gvbp0%+ztx8(@nibjdl4z46&sgj8%n7$8wo+bk-i6bnnjarg!x'

INSTALLED_APPS = (
    'ants',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}

# silence system check about unset `MIDDLEWARE_CLASSES`
SILENCED_SYSTEM_CHECKS = ['1_7.W001']
