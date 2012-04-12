#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import objectifier

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='objectifier',
    version=objectifier.__version__,
    url='http://git.elmcitylabs.com/objectifier',
    license=objectifier.__license__,
    description='Turns dictionaries into Python objects.',
    author=objectifier.__author__,
    author_email=objectifier.__email__,
    packages=['objectifier'],
    package_data={'': ['LICENSE']},
)

