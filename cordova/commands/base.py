#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os.path import abspath, exists, join

from cordova.version import __version__

class Command(object):

    def __init__(self, console):
        self.console = console

    @staticmethod
    def print_version():
        print 'PhoneGap - Cordova v%d.%d.%d' % __version__

    def run(self):
        raise NotImplementedError()

    def is_cordova_folder(self, path=None):
        if not path:
            path = abspath(os.curdir)

        return exists(join(path, 'www')) and exists(join(path, 'tmp'))

