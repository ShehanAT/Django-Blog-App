#!/user/bin/env python 

from distutils.core import setup 
from setuptools import setup, find_packages 

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-django',
    'pylint',
    'pylint_django',
    'git-pylint-commit-hook'
]

setup(
    name="django-blog-application",
    version="1.0",
    description="A simple blog application",
    author="Shehan Atukorala",
    author_email="shehanatuk@gmail.com",
    url="",
    packages=find_packages(include=['blogproject.*']),
    tests_require=TEST_REQUIREMENTS
)