#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from cordova.version import __version__

class Console(object):
    def __init__(self):
        arguments = sys.argv
        self.executable = arguments[0]
        self.command = arguments[1]

    def run(self):
        COMMANDS[self.command](self).run()

class Command(object):

    def __init__(self, console):
        self.console = console

    def run(self):
        raise NotImplementedError()

class VersionCommand(Command):

    def run(self):
        print 'PhoneGap - Cordova v%d.%d.%d' % __version__

COMMANDS = {
    'version': VersionCommand
}

if __name__ == '__main__':
    console = Console()
    console.run()

