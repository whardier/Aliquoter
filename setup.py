#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

import aliquoter

with open('README.md') as stream:
  long_desc = stream.read()

setup(
    name = aliquoter.__name__,
    version = aliquoter.__version__,
    author = aliquoter.__author__,
    author_email = aliquoter.__email__,
    packages = ['aliquoter'],
    license = aliquoter.__license__,
    description = aliquoter.__description__,
    url='https://github.com/whardier/Aliquoter',
    long_description = long_desc,
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)


