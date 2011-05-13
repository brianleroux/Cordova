#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from cordova.version import __version__

class Command(object):

    def __init__(self, console):
        self.console = console

    def run(self):
        raise NotImplementedError()

def print_version():
    print 'PhoneGap - Cordova v%d.%d.%d' % __version__

class VersionCommand(Command):
    key = 'version'

    def run(self):
        print_version()

    @staticmethod
    def print_overview():
        print '    version - show the currently installed version of Cordova'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap version'
        print
        print '    Retrieves the version for the Cordova library currently installed.'
        print
        print_version()

class HelpCommand(Command):
    key = 'help'

    def __init__(self, console, all_commands):
        super(HelpCommand, self).__init__(console)
        self.all_commands = all_commands

    def run(self):
        if not self.console.arguments:
            self.print_detailed_usage()
            return

        command_key = self.console.arguments[0]
        command = [command for command in self.all_commands if command.key == command_key]

        if not command or command_key == 'help':
            print "Error: command %s not found." % command_key
            print

            print 'Usage: phonegap help command'
            print

            print_version()
            sys.exit(1)

        command[0].print_detailed_usage()

    def print_detailed_usage(self):
        self.print_usage()
        print

        self.print_commands()

        print
        print "See 'phonegap help <command>' for more information on a specific command."
        print

        print_version()

    def print_usage(self):
        print 'Usage: phonegap command [options]'

    @staticmethod
    def print_overview():
        print '    help - show this help message and exit'

    def print_commands(self):
        print 'Available commands:'
        for command in self.all_commands:
            command.print_overview()

class ReadConfigCommand(Command):
    key = 'read-config'

    def run(self):
        print_version()

    @staticmethod
    def print_overview():
        print '    read-config - shows configuration for the current project'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap read-config configuration'
        print
        print '    Displays configuration values for the current project.'
        print
        print '    Available configurations:'
        print '        id - Returns the application id as specified by the name element in the config file.'
        print '        name - Returns the application name as specified in the config file.'
        print '        small-icon - Returns the path to the app\'s small icon.'
        print '        medium-icon - Returns the path to the app\'s medium icon.'
        print '        large-icon - Returns the path to the app\'s large icon.'
        print
        print_version()


