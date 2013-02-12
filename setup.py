#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'webpy-extras',
    version = '0.1',
    description = 'webpy-extras: extras for web.py',
    long_description = "Extras for building web.py applications",
    author = 'Joshua Barone',
    author_email = 'jbarone@justbecausesoftware.com',
    maintainer = 'Joshua Barone',
    maintainer_email = 'jbarone@justbecausesoftware.com',
    url = 'https://github.com/jbarone/webpy-extras',
    install_requires = 'web.py>=0.37',
    packages = ['extras'],
    license = 'GPLv3',
    test_suite = 'nose.collector',
    tests_require = ['nose>=1.2.1','coverage>=3.6'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
