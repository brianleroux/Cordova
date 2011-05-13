#!/usr/bin/python
# -*- coding: utf-8 -*-

from cordova.commands.base import Command

class VersionCommand(Command):
    key = 'version'

    def run(self):
        self.print_version()

    @staticmethod
    def print_overview():
        print '    version - show the currently installed version of Cordova'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap version'
        print
        print '    Retrieves the version for the Cordova library currently installed.'
        print
        cls.print_version()

