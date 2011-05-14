#!/usr/bin/python
# -*- coding: utf-8 -*-

from cordova.commands.help import HelpCommand
from cordova.commands.version import VersionCommand
from cordova.commands.read_config import ReadConfigCommand
from cordova.commands.validate_config import ValidateConfigCommand
from cordova.commands.version_index import VersionIndexCommand
from cordova.commands.find_plugin import FindPluginCommand

COMMANDS = [
    FindPluginCommand,
    ReadConfigCommand,
    ValidateConfigCommand,
    VersionIndexCommand,
    VersionCommand,
    HelpCommand,
]
