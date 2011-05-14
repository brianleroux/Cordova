#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import json
import urllib

from cordova.commands.base import Command

class Repository(object):
    def __init__(self, type, url):
        self.type = type
        self.url = url

class Plugin(object):
    def __init__(self, 
                 name, 
                 description, 
                 version, 
                 repository_type, 
                 repository_url,
                 author,
                 directories,
                 engines):
        self.name = name
        self.description = description
        self.version = version
        self.repository = Repository(repository_type, repository_url)
        self.author = author
        self.directories = directories
        self.engines = engines
    
    @classmethod
    def from_json(cls, item):
        return Plugin(item['name'], item['description'], item['version'], item['repository']['type'],
                      item['repository']['url'], item['author'], item['directories'], item['engines'])

    def simple_describe(self):
        return "%s v%s - %s" % (self.name, self.version, self.description)

    def detailed_describe(self):
        name = "%s v%s" % (self.name, self.version)
        name_separator = "-" * len(name)

        description = [
            name,
            name_separator,
            self.description,
            '',
            'Author: %s' % self.author,
            'Repository (%s): %s' % (self.repository.type, self.repository.url)
        ]

        return "\n".join(description)

class FindPluginCommand(Command):
    key = 'find-plugin'
    type = 'main'

    def run(self, config_path=None):
        try:
            url = 'http://phonegap-plugins.appspot.com/_je/plugin'
            plugins_json = urllib.urlopen(url).read()
            plugins = json.loads(plugins_json)
        except (ValueError, ):
            print "Connection to %s failed. Could not retrieve plugin list." % url
            sys.exit(1)

        plugin_list = []
        for index, item in enumerate(plugins):
            if not 'name' in item:
                continue
            plugin_list.append(Plugin.from_json(item))

        plugin_name = None
        if self.console.arguments:
            plugin_name = self.console.arguments[-1]

        if not plugin_name:
            print 'Listing all PhoneGap Plugins...'
            print

            for plugin in plugin_list:
                print '    %s' % plugin.simple_describe()

            print
            print "Type 'phonegap find-plugin <plugin name or part of plugin name>' to find more about it."

            print
            self.print_version()

        else:
            matching_plugins = [plugin for plugin in plugin_list if re.search(plugin_name.lower(), plugin.name.lower())]

            if not matching_plugins:
                print "No plugin found with a name that matches %s" % plugin_name
                sys.exit(1)

            for plugin in matching_plugins:
                print plugin.detailed_describe()

            print
            self.print_version()

    @staticmethod
    def print_overview():
        print '    find-plugin - shows informaton on a given plugin or lists all available plugins'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap find-plugin [plugin name]'
        print
        print '    Shows information on plugins. Displays information about one plugin if plugin name is specified.'
        print
        cls.print_version()


