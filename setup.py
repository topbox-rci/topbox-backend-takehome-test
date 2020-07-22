#!/usr/bin/env python
from setuptools import setup, find_packages

from app import __version__

setup(
    name='topbox-backend-takehome-test',
    version=__version__,
    description='Backend Take Home Test',
    url='topbox.io',
    install_requires=[
        'bson==0.5.10',
        'cachetools==4.1.1',
        'flask==1.1.2',
        'pymongo==3.10.1',
    ],
    test_suite='tests',
    packages=find_packages(exclude=('tests',)),
)
