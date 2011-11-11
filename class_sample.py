#!/usr/bin/env python

"""Sample classes

This script is just a sample for using classes in Python.

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2011-04-01'

from UserDict import UserDict


class SampleClass:

    """Just another sample class"""

    def __init__(self, spam=None):
        self.spam = spam

    def multiply(self, times=1):
        """Multiply a string."""
        return self.spam * times


class SampleDict(UserDict):

    """Class with ancestor class"""

    def __init__(self, name=None):
        UserDict.__init__(self)
        self['name'] = name


class SampleEasyDict(dict):

    """Sample descendant class with passed object type"""

    def __init__(self, name=None):
        self['name'] = name


class SampleCounter(dict):

    """Sample descendant class with passed object type and class attributes"""

    count = 0

    def __init__(self):
        self.__class__.count += 1
        try:
            self['instance_count']
        except KeyError:
            self['instance_count'] = 0
        self['instance_count'] += 1
