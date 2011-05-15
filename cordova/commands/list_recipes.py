#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os.path import abspath, join, dirname, split, exists, expanduser

from cordova.commands.base import Command

class ListRecipesCommand(Command):
    key = 'list-recipes'
    type = 'main'

    def run(self):
        root_path = abspath(join(dirname(__file__), '..', '..', 'recipes'))
        places_to_look = [root_path]

        home_recipes = abspath('%s/phonegap/recipes' % expanduser('~'))
        if exists(home_recipes):
            places_to_look.append(home_recipes)

        if 'PHONEGAP_RECIPES' in os.environ and exists(os.environ['PHONEGAP_RECIPES']):
            places_to_look.append(os.environ['PHONEGAP_RECIPES'])

        print 'Available recipes:'
        print

        for place_to_look in places_to_look:
            for directory in os.listdir(place_to_look):
                print '    %s' % split(directory)[-1]

        print
        self.print_version()

    @staticmethod
    def print_overview():
        print '    list-recipes - lists the available recipes for starting a new project'

    @classmethod
    def print_detailed_usage(cls):
        print 'Usage: phonegap list-recipes'
        print
        print '    Lists the available recipes for starting a new project.'
        print '    PhoneGap looks at its own recipes directory, as well as ~/phonegap/recipes'
        print '    and any folder specified under the environment variable PHONEGAP_RECIPES.'
        print
        cls.print_version()


