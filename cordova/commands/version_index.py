#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
from os.path import abspath, join, exists

from cordova.commands.base import Command
from cordova.commands.read_config import ReadConfigCommand

class VersionIndexCommand(Command):
    key = 'version-index'

    def run(self, config_path=None, index_path=None):
        if self.console.arguments and self.console.arguments[-1].endswith('index.html'):
            index_path = abspath(join('.', self.console.arguments.pop()))

        if self.console.arguments and self.console.arguments[-1].endswith('config.xml'):
            config_path = abspath(join('.', self.console.arguments.pop()))

        if not config_path:
            config_path = abspath(join(os.curdir, 'www', 'config.xml'))

        if not index_path:
            index_path = abspath(join(os.curdir, 'www', 'index.html'))

        if not exists(config_path):
            print 'The configuration file %s was not found!' % config_path
            sys.exit(1)

        if not exists(index_path):
            print 'The main PhoneGap file %s was not found!' % config_path
            sys.exit(1)

        values = ReadConfigCommand.get_values(config_path)

        expr = '<div id="version">.*?</div>'
        new_version = '<div id="version">' + values['version'] + '</div>'

        reader = open(index_path, 'r')
        index = reader.read()
        match = re.search(expr, index)

        if match:
            tmp = re.sub(expr, new_version, index)
        else:
            tmp = index.replace('</body>', new_version + '</body>')

        reader.close()

        writer = open(index_path, 'w')
        writer.write(tmp)
        writer.close()

    @staticmethod
    def print_overview():
        print '    version-index - Includes the version in the index.html file.'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap version-index [configuration file] [index file]'
        print
        print '    Includes the current version number in the index.html file.'
        print
        cls.print_version()


