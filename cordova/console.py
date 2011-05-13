#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from cordova.version import __version__

class Console(object):
    def __init__(self):
        arguments = sys.argv
        self.executable = arguments[0]
        if len(arguments) < 2:
            self.command = 'help'
        else:
            self.command = arguments[1]

        self.arguments = []
        if (len(arguments) > 2):
            self.arguments = arguments[2:]

    def run(self):
        command = [command for command in COMMANDS if command.key == self.command]
        if command:
            command[0](self).run()
        else:
            HelpCommand(self).run()

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

class HelpCommand(Command):
    key = 'help'

    def run(self):
        self.print_usage()
        print

        if not self.console.arguments:
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
        print "Available commands:"
        for command in COMMANDS:
            command.print_overview()

COMMANDS = [
    VersionCommand,
    HelpCommand
]

if __name__ == '__main__':
    console = Console()
    console.run()

