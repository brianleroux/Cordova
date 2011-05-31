#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from cordova.commands.base import Command

class InstallPluginCommand(Command):
    key = 'install-plugin'
    type = 'main'

    def run(self):
        if not self.console.arguments:
            print 'ERROR: The plugin name is mandatory!'
            print
            self.print_version()
            sys.exit(1)

        plugin_list = self.get_all_plugins()
        plugin = plugin_list.find_by_key(self.console.arguments)
        if not plugin:
            print 'ERROR: The plugin with key %s was not found!'
            print
            self.print_version()

    @staticmethod
    def print_overview():
        print '    install-plugin - install the specified plugin in the current PhoneGap project.'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap install-plugin [plugin name]'
        print
        print '    Install the specified plugin in the current PhoneGap project.'
        print
        cls.print_version()


