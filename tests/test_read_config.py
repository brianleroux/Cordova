#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import abspath, join, dirname
import commands

read_config_path = abspath(join(dirname(__file__), '../generate-template/bin/util/read-config'))
read_config = lambda option: commands.getoutput('%s %s tests/config.xml' % (read_config_path, option))

tests = {
    'id': 'com.phonegap.vanilla',
    'version': '0.0.0',
    'name': 'PhoneGap Vanilla',
    'small-icon': './www/img/icon-57.png',
    'medium-icon': './www/img/icon-72.png',
    'large-icon': './www/img/icon-114.png'
}

def test_configurations():
    for key, value in tests.iteritems():
        yield verify_configuration, key, value

def verify_configuration(configuration, expected):
    config_value = read_config(configuration)

    assert config_value == expected, config_value

