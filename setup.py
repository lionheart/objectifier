#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import os
from objectifier import metadata

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst") as file:
    long_description = file.read()

setup(
    name='objectifier',
    version=metadata.__version__,
    url='https://github.com/elmcitylabs/objectifier',
    license=metadata.__license__,
    long_description=long_description,
    description='Objectifier makes it easy to inspect and traverse Python objects.',
    author=metadata.__author__,
    author_email=metadata.__email__,
    packages=['objectifier'],
    test_suite='objectifier.tests',
    package_data={'': ['LICENSE', 'README.rst']}
)

