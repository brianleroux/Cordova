#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import join, abspath, dirname
import commands

from pyvows import Vows, expect

from cordova.version import __version__

root_path = abspath(join(dirname(__file__), '../'))
console_app = join(root_path, 'cordova', 'console.py')
execute = lambda command: commands.getoutput('python %s %s' % (console_app, command))

@Vows.batch
class ConsoleApp(Vows.Context):

    class VersionCommand(Vows.NotErrorContext, Vows.NotEmptyContext):

        def topic(self):
            return execute('version')

        def should_be_equal_to_version(self, topic):
            expect(topic).to_be_like('PhoneGap - Cordova v%d.%d.%d' % __version__)

    #class HelpCommand(Vows.NotErrorContext, Vows.NotEmptyContext):

        #def topic(self):
            #return execute('help')

