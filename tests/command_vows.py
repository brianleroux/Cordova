#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyvows import Vows, expect

from cordova.commands.base import Command

@Vows.batch
class CommandVows(Vows.Context):

    class BaseCommandVows(Vows.Context):
        def topic(self):
            return Command(self).run()

        def should_be_an_error(self, topic):
            expect(topic).to_be_an_error()

        def should_be_not_implemented_error(self, topic):
            expect(topic).to_be_an_error_like(NotImplementedError)

