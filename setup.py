#!/usr/bin/env python

from distutils.core import setup

setup(name='bencoder',
      version='0.2.1',
      description='A simple bencode decoder/encoder library in pure Python.',
      url='https://github.com/utdemir/bencoder',
      author='Utku Demir',
      author_email='utdemir@gmail.com',
      py_modules=['bencoder'],
      classifiers=[
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ],
      )
