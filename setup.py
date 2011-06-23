# -*- coding:utf-8 -*-

from setuptools import setup
from setuptools import find_packages

from __init__ import __version__, __license__, __author__, __email__

setup(
    name         = 'attrcheck',
    version      = __version__,
    description  = 'A simple attribution checker implemented as a decorator',
    long_description = '''
attrcheck: attribution checker

This module provides a simple attribution checker implemented as a decorator.
All functionality are provided as keyword arguments of the decorator.
    ''',
    author       = __author__,
    author_email = __email__,
    url          = 'https://github.com/jnamika/attrcheck',
    license      = __license__,
    keywords     = 'argument check hasattr decorator',
    packages     = find_packages(),
    test_suite = 'test_attrcheck.suite',
    classifiers  = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: %s' % __license__,
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
