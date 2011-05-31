#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from cordova.commands import COMMANDS, HelpCommand

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

        if command and self.command != 'help':
            command[0](self).run()
        else:
            HelpCommand(self, COMMANDS).run()

        sys.exit(0)

def main():
    console = Console()
    console.run()

if __name__ == '__main__':
    main()
