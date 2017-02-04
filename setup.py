import codecs
import os
import sys
from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


def readme():
    return read("./README.md")

VERSION = "0.0.7"

CONF_PATH = "ants/conf"

requires = ["Django>=1.10.2", "gevent>=1.1.1"]

EXCLUDE_FROM_PACKAGES = ['test_settings',
                         'ants.conf']

setup(
    name='ants',
    version=VERSION,
    description='A human spider framework base on django',
    long_description=readme().strip(),
    author='mymusise',
    author_email='mymusise1@gmail.com',
    url='https://github.com/mymusise/ants',
    license='MIT',
    scripts=['bin/ants-tools.py'],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords='spider django human',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ],
    zip_safe=False,
    install_requires=requires,
)
