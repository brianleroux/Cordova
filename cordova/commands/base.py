#!/usr/bin/python
# -*- coding: utf-8 -*-

from cordova.version import __version__

class Command(object):

    def __init__(self, console):
        self.console = console

    @staticmethod
    def print_version():
        print 'PhoneGap - Cordova v%d.%d.%d' % __version__

    def run(self):
        raise NotImplementedError()

