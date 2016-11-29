import codecs
import os
import sys
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


def readme():
    return read("./README.txt")

VERSION = "1.0.4"

setup(
    name='ants',
    version=VERSION,
    description='A human spider framework base on django',
    long_description=readme().strip(),
    author='mymusise',
    author_email='mymusise1@gmail.com',
    url='https://github.com/mymusise/ants',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
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
    include_package_data=True,
    package_data={
        '': ['.README.md']
    },
    zip_safe=False,
)
