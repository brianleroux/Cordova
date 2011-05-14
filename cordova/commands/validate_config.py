#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from xml.parsers.expat import ExpatError

from os.path import abspath, join, exists

from cordova.commands.base import Command
from cordova.commands.read_config import ReadConfigCommand

class ValidateConfigCommand(Command):
    key = 'validate-config'

    def run(self, config_path=None):
        if self.console.arguments:
            config_path = abspath(join('.', self.console.arguments[-1]))

        if not config_path:
            config_path = abspath(join(os.curdir, 'www', 'config.xml'))

        if not exists(config_path):
            print 'The configuration file %s was not found!' % config_path
            sys.exit(1)

        try:
            values = ReadConfigCommand.get_values(config_path)
        except ExpatError:
            print 'The configuration file at %s is not well formed!' % config_path
            sys.exit(1)

        if 'id' not in values or not values['id']:
            print 'The configuration file at %s is missing an id attribute!' % config_path
            sys.exit(1)

        if 'name' not in values or not values['name']:
            print 'The configuration file at %s is missing a name attribute!' % config_path
            sys.exit(1)

        if 'version' not in values or not values['version']:
            print 'The configuration file at %s is missing a version attribute!' % config_path
            sys.exit(1)

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


