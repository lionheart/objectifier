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
    url='http://elmcitylabs.com',
    license='Apache 2.0',
    description='Turns dictionaries into Python objects.',
    author='Dan Loewenherz',
    author_email='dan@elmcitylabs.com',
    packages=['objectifier'],
    package_data={'': ['LICENSE']},
)

