#!/usr/bin/env python

from distutils.core import setup
from extras import __version__

setup(name='webpy-extras',
      version=__version__,
      description='webpy-extras: extras for web.py',
      author='Joshua Barone',
      author_email='jbarone@justbecausesoftware.com',
      maintainer='Joshua Barone',
      maintainer_email='jbarone@justbecausesoftware.com',
      url=' http://webpy-extras.justbecausesoftware.com/',
      packages=['extras'],
      long_description="Extras for building web.py applications",
      license="Public domain",
      platforms=["any"],
     )

