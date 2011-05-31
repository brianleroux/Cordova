#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from cordova.version import format_version

setup(
    name = 'cordova',
    version = format_version(),
    description = "Top secret but not so secret PhoneGap buildchain for OS X",
    long_description = """
A PhoneGap project toolchain that automates common tasks for building cross platform mobile projects with OS X.

Automate common development workflow tasks such as: compiling, debugging, testing, releasing and other things in between. As an added benefit projects generated with Cordova create a consistent, predictable, easy to understand and therefor extend software project. A number of conventions are introduced removing the need for mobile developers to relearn their tools or, worse, rebuild them for every project.""",
    keywords = 'Mobile PhoneGap Cordova Web',
    author = 'Brian LeRoux',
    author_email = 'brian.leroux@westcoastlogic.com',
    url = 'http://www.phonegap.com',
    license = 'https://github.com/heynemann/Cordova/blob/master/LICENSE',
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Natural Language :: English',
                   'Operating System :: MacOS',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.6'],
    packages = find_packages(),
    package_dir = {"cordova": "cordova"},
    include_package_data = True,

    package_data = {
        'cordova': ['*.*'],
    },

    entry_points = {
        'console_scripts': [
            'phonegap = cordova.console:main',
        ],
    },

)


