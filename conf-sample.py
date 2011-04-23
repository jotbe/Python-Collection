#!/usr/bin/env python

"""Read and write configuration files

This script is an example for a config parser

== Use cases ==

- Read a default config from a template
- Edit and add config sections and items
- Write changed values to config file

== Sample config ==

# Test config for conf.py, save it as 'conf.ini'
[global]
spam = Ni!
eggs = foo, bar
max_eggs = 10

[specific]
max_knights = 15

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2011-03-31'

import ConfigParser
import io
from types import *

if __name__ == '__main__':
    confFile = 'conf.ini'
    conf = """
[global]
spam = Ni!
eggs = foo, bar
max_eggs = 5
skip_bridge

[specific]
max_knights = 15
    """

    config = ConfigParser.RawConfigParser(allow_no_value = True)

    #config.read(confFile)
    config.readfp(io.BytesIO(conf))
    """Read the config
    Invert the comments of the two lines above if you want to read
    from confFile
    
    """

    print config.get('global', 'eggs').split(',')
    print 'Max eggs: ', config.getint('global', 'max_eggs')
    # Get item without value, returns either True or False
    print 'Skip bridge: ', (type(config.get('global', 'skip_bridge')) == NoneType)

    # Add new section
    sec = 'new_section'
    try:
        config.add_section(sec)
    except ConfigParser.DuplicateSectionError:
        print 'Section %s exists ... updating ...' % sec

    config.set('new_section', 'life', 'brian')
    config.set('new_section', 'favorite_color', 'blue')

    # Edit existing section
    config.set('global', 'max_eggs', 20)
    print 'Max eggs: ', config.getint('global', 'max_eggs')

    # Write to file
    with open(confFile, 'wb') as configfile:
            config.write(configfile)

    print 'Done.'