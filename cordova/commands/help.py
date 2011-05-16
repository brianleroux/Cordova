#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from cordova.commands.base import Command

class HelpCommand(Command):
    key = 'help'
    type = 'system'

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

            self.print_version()
            sys.exit(1)

        command[0].print_detailed_usage()

    def print_detailed_usage(self):
        self.print_usage()
        print

        self.print_commands()

        print
        print "See 'phonegap help <command>' for more information on a specific command."
        print

        self.print_version()

    def print_usage(self):
        print 'Usage: phonegap command [options]'

    @staticmethod
    def print_overview():
        print '    help - show this help message and exit.'

    def print_commands(self):
        print 'Available commands:'
        for command in filter(lambda c: c.type == 'main', self.all_commands):
            command.print_overview()

        print
        print 'Utilities:'
        for command in filter(lambda c: c.type == 'util', self.all_commands):
            command.print_overview()

        print
        print 'Other commands:'
        for command in filter(lambda c: c.type == 'system', self.all_commands):
            command.print_overview()

