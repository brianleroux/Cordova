#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from os.path import abspath, join

from cordova.commands.base import Command

class ValidateConfigCommand(Command):
    key = 'validate-config'

    def run(self, config_path=None):
        if not config_path:
            config_path = abspath(join(os.curdir, 'www', 'config.xml'))

        values = ReadConfigCommand.get_values(config_path)

    @staticmethod
    def print_overview():
        print '    validate-config - Validates the configuration file for the current project.'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap validate-config'
        print
        print '    Validates the configuration file for the current project.'
        print
        cls.print_version()


