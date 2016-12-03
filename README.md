Ants
===

Ants is a clawer framework for perfectionism base on Django， which help people build a clawer faster and easier to make manage.


Requirements
===

- Python 2.7 +
- Django 1.10 +
- Gevent 1.1.2 
- Jinja2 2.8


Install 
===

	pip install ants
    
To get the lastest, download this fucking source code and build

	git clone git@github.com:mymusise/Ants.git
    cd Ants
    python setup.py build
    sudo python setup.py install
    


Getting started
====

## 1. Initialize project

Ok, I suggest you work on a virtualenv

	virtualenv my_env
    source my_env/bin/activate

Then we install the Requirements and start a django project

	pip install django gevent ants
    django-admin startproject my_ants
    cd my_ants
    

In Ants, download and parser is divided. It mean there is two part of Ants, ``clawers`` and ``parsers``

	python manage.py startapp clawers
    mkdir spider/ants
    touch spider/ants/__init__.py
    python manage.py startapp parsers
    mkdir parsers/ants
    touch parsers/ants/__init__.py

##### ! More sample to do ``ants-tools startproject my_ants`` (not complete yead)


### 2. settings.py

Add apps in your my_ants/settings.py

	...
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'clawers', ###
        'parsers', #  what you need to add
        'ants',    ###
    ]
    ...
    

### 3. Write your first spider ant!

Ants will run ants belong to clawers by run command `python manage.py runclawer [spider_name]`

Let's add a ant.``spider/ants/first_blood.py``

    from ants.utils import BaseMixin
    import requests


    class FirstBloodClawerWhatNameYouWant(BaseMixin):
        NAME = 'first_blood'
        url_head = """https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=10&page_start={}"""
        max_page = 4

        def get_url(self, url):
            res = requests.get(url)
            print(res.text)

        def start(self):
            need_urls = [self.url_head.format(i) for i in range(self.max_page)]
            list(map(self.get_url, need_urls))


This is a simple spider that can get hot movie from `Douban`.
Be attention, the `NAME` property is required, which is the unique identification
for different clawers.

Now we can run our first blood to get hot movie!

	python manage.py runclawer first_blood


# Enjoy!