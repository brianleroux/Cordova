#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import join, abspath, dirname
from optparse import OptionParser

from cordova.commands.base import Command

class CreateCommand(Command):
    key = 'create'
    type = 'main'

    def run(self):
        root_path = abspath(join(dirname(__file__), '..', '..'))
        parser = OptionParser()

        parser.add_option("-w", "--www", action="store", 
                          dest="www", default="vanilla",
                          help="recipe for www")

        parser.add_option("-t", "--test", action="store", 
                          dest="test", default="qunit",
                          help="recipe for test directory")

        options, args = parser.parse_args(self.console.arguments)

        try:
            prj = args[0]
            www = os.path.join(os.path.dirname(__file__), 'recipes', options.www)
            test = os.path.join(os.path.dirname(__file__), 'recipes', options.test)
            tmpl = os.path.join(os.path.dirname(__file__), 'generate-template')
            dest =  os.path.join(os.getcwd(), prj)
            dest_www = os.path.join(dest, 'www')
            dest_test = os.path.join(dest, 'test')
            # copy in the new project yay!
            os.system("cp -r " + tmpl + " " + dest)
            # clobber crummy local www
            os.system('rm -rf ' + dest_www)
            os.system('rm -rf ' + dest_test)
            # copy in recipes for www and test 
            os.system("cp -r " + www + " " + dest_www)
            os.system("cp -r " + test + " " + dest_test)
        except:
            print 'error: please supply a project name'

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


