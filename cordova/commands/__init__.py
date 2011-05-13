#!/usr/bin/python
# -*- coding: utf-8 -*-

from cordova.commands.help import HelpCommand
from cordova.commands.version import VersionCommand
from cordova.commands.read_config import ReadConfigCommand

COMMANDS = [
    ReadConfigCommand,
    VersionCommand,
    HelpCommand
]
