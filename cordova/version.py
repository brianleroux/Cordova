#!/usr/bin/python
# -*- coding: utf-8 -*-

# having the version as a tuple makes some automation easier
__version__ = (0, 1, 0)

def format_version():
    return ".".join([str(digit) for digit in __version__])
