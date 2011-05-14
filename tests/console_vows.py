#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import join, abspath, dirname
import commands

from pyvows import Vows, expect

from cordova.version import __version__

root_path = abspath(join(dirname(__file__), '../'))
console_app = join(root_path, 'cordova', 'console.py')
execute = lambda command: commands.getstatusoutput('python %s %s' % (console_app, command))

class DefaultContext(Vows.NotErrorContext, Vows.NotEmptyContext):
    pass

@Vows.batch
class ConsoleApp(Vows.Context):

    class VersionCommand(DefaultContext):

        def topic(self):
            return execute('version')[1]

        def should_be_equal_to_version(self, topic):
            expect(topic).to_be_like('PhoneGap - Cordova v%d.%d.%d' % __version__)

    class HelpCommand(DefaultContext):

        def topic(self):
            return execute('help')[1]

        def should_include_version(self, topic):
            expect(topic).to_include('PhoneGap - Cordova v%d.%d.%d' % __version__)

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap command [options]')

        def should_include_list_of_commands(self, topic):
            expect(topic).to_include('Available commands:')

        def should_include_version_command(self, topic):
            expect(topic).to_include('version - show the currently installed version of Cordova')

        def should_include_help_command(self, topic):
            expect(topic).to_include('    help - show this help message and exit')

    class HelpVersion(DefaultContext):

        def topic(self):
            return execute('help version')[1]

        def should_include_version(self, topic):
            expect(topic).to_include('PhoneGap - Cordova v%d.%d.%d' % __version__)

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap version')

        def should_include_version_explanation(self, topic):
            expect(topic).to_include('Retrieves the version for the Cordova library currently installed.')

    class HelpCommandError(DefaultContext):

        def topic(self):
            return execute('help wtf')[1]

        def should_return_error_message(self, topic):
            expect(topic).to_include('Error: command wtf not found.')

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap help command')

    class HelpValidateConfig(DefaultContext):

        def topic(self):
            return execute('help validate-config')[1]

        def should_include_version(self, topic):
            expect(topic).to_include('PhoneGap - Cordova v%d.%d.%d' % __version__)

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap validate-config')

        def should_include_explanation(self, topic):
            expect(topic).to_include('Validates the configuration file for the current project.')

    class HelpReadConfig(DefaultContext):

        def topic(self):
            return execute('help read-config')[1]

        def should_include_version(self, topic):
            expect(topic).to_include('PhoneGap - Cordova v%d.%d.%d' % __version__)

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap read-config [configuration]')

        def should_include_explanation(self, topic):
            expect(topic).to_include('Displays configuration values for the current project.')

        def should_include_available_configurations(self, topic):
            expect(topic).to_include('Available configurations:')

        def should_include_id(self, topic):
            expect(topic).to_include('id - Returns the application id as specified by the name element in the config file.')

        def should_include_name(self, topic):
            expect(topic).to_include('name - Returns the application name as specified in the config file.')

        def should_include_small_icon(self, topic):
            expect(topic).to_include('small-icon - Returns the path to the app\'s small icon.')

        def should_include_medium_icon(self, topic):
            expect(topic).to_include('medium-icon - Returns the path to the app\'s medium icon.')

        def should_include_large_icon(self, topic):
            expect(topic).to_include('large-icon - Returns the path to the app\'s large icon.')

    class ReadConfig(Vows.Context):

        class WithNoConfigs(DefaultContext):
            def topic(self):
                return commands.getoutput('cd tests/ && env PYTHONPATH=$PYTHONPATH:.. python %s %s' % (console_app, 'read-config'))

            def should_include_id(self, topic):
                expect(topic).to_include('id = com.phonegap.vanilla')

            def should_include_name(self, topic):
                expect(topic).to_include('name = PhoneGap Vanilla')

            def should_include_small_icon(self, topic):
                expect(topic).to_include('icon for 57px = ./www/img/icon-57.png')

            def should_include_medium_icon(self, topic):
                expect(topic).to_include('icon for 72px = ./www/img/icon-72.png')

            def should_include_large_icon(self, topic):
                expect(topic).to_include('icon for 114px = ./www/img/icon-114.png')

        class WithId(DefaultContext):
            def topic(self):
                return commands.getoutput('cd tests/ && env PYTHONPATH=$PYTHONPATH:.. python %s read-config id' % console_app)

            def should_include_id(self, topic):
                expect(topic).to_equal('com.phonegap.vanilla')

        class WithName(DefaultContext):
            def topic(self):
                return commands.getoutput('cd tests/ && env PYTHONPATH=$PYTHONPATH:.. python %s read-config name' % console_app)

            def should_include_id(self, topic):
                expect(topic).to_equal('PhoneGap Vanilla')

        class WithSmallIcon(DefaultContext):
            def topic(self):
                return commands.getoutput('cd tests/ && env PYTHONPATH=$PYTHONPATH:.. python %s read-config small-icon' % console_app)

            def should_include_id(self, topic):
                expect(topic).to_equal('./www/img/icon-57.png')

        class WithMediumIcon(DefaultContext):
            def topic(self):
                return commands.getoutput('cd tests/ && env PYTHONPATH=$PYTHONPATH:.. python %s read-config medium-icon' % console_app)

            def should_include_id(self, topic):
                expect(topic).to_equal('./www/img/icon-72.png')

        class WithLargeIcon(DefaultContext):
            def topic(self):
                return commands.getoutput('cd tests/ && env PYTHONPATH=$PYTHONPATH:.. python %s read-config large-icon' % console_app)

            def should_include_id(self, topic):
                expect(topic).to_equal('./www/img/icon-114.png')

    class ValidateConfig(Vows.Context):

        class WhenConfigDoesNotExist(Vows.Context):
            def topic(self):
                return execute('validate-config')

            def should_be_an_error(self, topic):
                expect(topic[0]).to_equal(256)

        class WhenItExists(Vows.Context):

            class ItShouldWork(Vows.Context):
                def topic(self):
                    return execute('validate-config tests/config.xml')[0]

                def should_not_be_an_error(self, topic):
                    expect(topic).to_equal(0)

            class AndFailWhenMalformed(Vows.Context):
                def topic(self):
                    return execute('validate-config tests/malformed_config.xml')

                def should_have_failure_status_code(self, topic):
                    expect(topic[0]).to_equal(256)

                def should_have_message_explaining_error(self, topic):
                    expect(topic[1]).to_include('The configuration file at')
                    expect(topic[1]).to_include('is not well formed!')

            class AndFailWhenMissingId(Vows.Context):
                def topic(self):
                    return execute('validate-config tests/missing_id_config.xml')

                def should_have_failure_status_code(self, topic):
                    expect(topic[0]).to_equal(256)

                def should_have_message_explaining_error(self, topic):
                    expect(topic[1]).to_include('The configuration file at')
                    expect(topic[1]).to_include('is missing an id attribute!')

            class AndFailWhenMissingName(Vows.Context):
                def topic(self):
                    return execute('validate-config tests/missing_name_config.xml')

                def should_have_failure_status_code(self, topic):
                    expect(topic[0]).to_equal(256)

                def should_have_message_explaining_error(self, topic):
                    expect(topic[1]).to_include('The configuration file at')
                    expect(topic[1]).to_include('is missing a name attribute!')

            class AndFailWhenMissingVersion(Vows.Context):
                def topic(self):
                    return execute('validate-config tests/missing_version_config.xml')

                def should_have_failure_status_code(self, topic):
                    expect(topic[0]).to_equal(256)

                def should_have_message_explaining_error(self, topic):
                    expect(topic[1]).to_include('The configuration file at')
                    expect(topic[1]).to_include('is missing a version attribute!')


