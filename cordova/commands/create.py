#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, abspath, dirname
from optparse import OptionParser
import shutil

from cordova.commands.base import Command

class CreateCommand(Command):
    key = 'create'
    type = 'main'

    def run(self):
        root_path = abspath(join(dirname(__file__), '..', '..'))
        recipes_path = join(root_path, 'recipes')

        parser = OptionParser()

        parser.add_option('-w', '--www', action='store', 
                          dest='www', default='vanilla',
                          help='recipe for www')

        parser.add_option('-t', '--test', action='store', 
                          dest='test', default='qunit',
                          help='recipe for test directory')

        options, args = parser.parse_args(self.console.arguments)

        if not args:
            print 'ERROR: The project name is required!'
            print
            print 'Type "phonegap help create" for more information.'
            print
            self.print_version()
            sys.exit(1)

        prj = args[0]

        www = join(recipes_path, options.www)
        test = join(recipes_path, options.test)

        tmpl = join(root_path, 'generate-template')
        dest =  abspath(join(os.curdir, prj))
        dest_www = join(dest, 'www')
        dest_test = join(dest, 'test')

        # copy in the new project yay!
        shutil.copytree(tmpl, dest)

        # clobber crummy local www
        shutil.rmtree(dest_www)
        shutil.rmtree(dest_test)

        # copy in recipes for www and test 
        shutil.copytree(www, dest_www)
        shutil.copytree(test, dest_test)

        print 'Project %s was created successfully!' % prj
        print
        print 'Don\'t forget to edit the config.xml file under www.'
        print 'Use ./bin/emulate to fire all emulators and ./bin/debug to install and debug your app.'
        print 'Explore the ./bin/ for more options.'
        print 'Happy hacking!'

    @staticmethod
    def print_overview():
        print '    create - starts a new PhoneGap project'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap create [project name] [-w WWW_TEMPLATE, --www=WWW_TEMPLATE] [-t TEST_TEMPLATE, --test=TEST_TEMPLATE]'
        print
        print '    Starts a new PhoneGap project named after project name.'
        print '    The www template is optional and defaults to the vanilla template.'
        print '    The test template is also optional and defaults to qunit.'

        print
        cls.print_version()


