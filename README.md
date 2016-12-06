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
    ants-tools  startproject my_ants
    cd my_ants
    
now you can use ``tree`` command to get the file-tree of your project

    ├── manage.py
    ├── my_ants
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── parsers
    │   ├── admin.py
    │   ├── ants
    │   │   └── __init__.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── spiders
        ├── admin.py
        ├── ants
        │   └── __init__.py
        ├── apps.py
        ├── __init__.py
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py



### 2. Write your first spider ant!

Ants will run ants belong to clawers by run command `python manage.py runclawer [spider_name]`

Let's add a ant.``spider/ants/first_blood.py``

    import requests


    class FirstBloodClawerWhatNameYouWant(object):
        NAME = 'first_blood' # must be unique
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


# About repeating URL

Ants provide a way to avoid running a same url again if Ants it crash last time. You just need define two model, source and aim. For example:

In file clawers/models.py 

    class BaseTask(models.Model):
        source_url = models.CharField(max_length=255)


    class MovieHtml(models.Model):
        task_id = models.IntegerField()
        html = models.TextField()

We define `BaseTask` to save the base task url we need request, and save the html source in `MovieHtml`. If we get a page by requesting a url from BaseTask, we will save this `BaseTask().id` to `MovieHtml().task_id`. We can redefine the our 'first_blood' ant like this:

    from ants.clawer import Clawer
    import requests

    class FirstBloodClawerWhatNameYouWant(Clawer):
        NAME = 'first_blood' # must be unique
        thread = 2 # the number of coroutine, default 1
        task_model = BaseTask
        goal_model = MovieHtml

        def run(self, task):
            res = requests.get(task.source_url)
            MovieHtml.objects.create(task_id=task.id, html=res.text)

Before 'first_blood'.run(), it will get all BaseTask objects and give each of then to run() function. But if one of BaseTask object.ID has in MovieHtml.task_id, this BaseTask object would be given to run function.

# About async

Ants use `gevent` as event pool to make each ant run with async, and you can use `thread` property to decide how many coroutine you want. More infomation from [the fucking source code](https://github.com/mymusise/Ants/blob/master/ants/utils.py#L74)

# Enjoy!