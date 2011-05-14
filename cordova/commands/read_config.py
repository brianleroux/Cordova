#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from xml.dom.minidom import parse

from os.path import abspath, join

from cordova.commands.base import Command

class ReadConfigCommand(Command):
    key = 'read-config'

    def run(self, config_path=None):
        if not config_path:
            config_path = abspath(join(os.curdir, 'www', 'config.xml'))

        values = self.get_values(config_path)

        if not self.console.arguments:
            print "id = %s" % values['id']
            print "name = %s" % values['name']
            print "version = %s" % values['version']

            for icon in values['icons']:
                print "icon for %dpx = %s" % (icon[1], icon[0])
            return

        config_name = self.console.arguments[0]

        if config_name in ('id', 'name'):
            print values[config_name]
            return

        if config_name == 'small-icon':
            print values['icons'][-1][0]
            return

        if config_name == 'medium-icon':
            print values['icons'][1][0]
            return

        if config_name == 'large-icon':
            print values['icons'][0][0]
            return

    @classmethod
    def get_values(cls, config_path):
        parsed = parse(config_path)

        id_value = parsed.firstChild.getAttribute('id')
        version = parsed.firstChild.getAttribute('version')

        name_elements = parsed.getElementsByTagName('name')
        name = ''
        if name_elements:
            name = name_elements.pop().firstChild.nodeValue

        return {
            'id': id_value,
            'version': version,
            'name': name,
            'icons': cls.get_icons(parsed)
        }

    @classmethod
    def get_icons(cls, parsed):
        # icons logic
        icons = []
        tmp_icons = parsed.getElementsByTagName('icon')
        # create a list of tuples (icon_path, icon_width)
        for index, item in enumerate(tmp_icons):
            src = item.attributes.get('src', None)
            if src:
                src = src.value

            width = item.attributes.get('width', 0)
            if width:
                width = int(width.value)

            # shouldn't add icons that fail to provide src attribute
            if src:
                icons.append((join('.', 'www', src), int(width)))

        # sort largest icon to smallest
        def comparer(a, b):
            if a[1] > b[1]:
                return -1
            elif a[1] == b[1]:
                return 0
            else:
                return 1
        # finally set the sorted icons tuple list
        icons = sorted(icons, comparer)

        return icons

    @staticmethod
    def print_overview():
        print '    read-config - shows configuration for the current project'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap read-config [configuration]'
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
        cls.print_version()


