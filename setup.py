# -*- coding:utf-8 -*-

from setuptools import setup

import sys
sys.path.append('src')

from src import __version__, __license__, __author__, __email__, __doc__

setup(
    name         = 'attrcheck',
    version      = __version__,
    description  = 'A simple attribution checker implemented as a decorator',
    long_description = __doc__,
    author       = __author__,
    author_email = __email__,
    url          = 'https://github.com/jnamika/attrcheck',
    license      = __license__,
    keywords     = 'argument check hasattr decorator',
    packages     = ['attrcheck'],
    package_dir  = {'attrcheck' : 'src'},
    test_suite   = 'test_attrcheck',
    classifiers  = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: %s' % __license__,
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
