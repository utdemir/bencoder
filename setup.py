#!/usr/bin/env python

from distutils.core import setup

setup(name='bencoder',
      version='0.2.0',
      description='A simple bencode decoder/encoder library in pure Python.',
      url='https://github.com/utdemir/bencoder',
      author='Utku Demir',
      author_email='utdemir@gmail.com',
      py_modules=['bencoder'],
      classifiers=[
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ],
      )
