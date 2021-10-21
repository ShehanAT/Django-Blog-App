#!/user/bin/env python 

from distutils.core import setup 
from setuptools import setup, find_packages 

setup(
    name="django-blog-application",
    version="1.0",
    description="A simple blog application",
    author="Shehan Atukorala",
    author_email="shehanatuk@gmail.com",
    url="",
    pacakges=find_packages(include=['blogproject.*']),
)