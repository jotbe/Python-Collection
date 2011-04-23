#!/usr/bin/env python

"""Instantiating classes in Python

This script is a sample for instantiating some sample classes.

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2011-04-01'

import class_sample

if __name__ == '__main__':
    print dir(class_sample)

    # SampleClass
    print '\n= SampleClass ='
    my_class = class_sample.SampleClass('456')

    print my_class.spam
    print my_class.multiply(2)

    # SampleDict
    print '\n= SampleDict ='
    my_dict = class_sample.SampleDict(name='eggs')

    print my_dict['name']
    print my_dict

    print '%(name)s are not Spam' % my_dict

    print 'Keys: ', my_dict.keys()
    print 'Values: ', my_dict.values()
    print 'Items: ', my_dict.items()

    # SampleEasyDict
    print '\n= SampleEasyDict ='
    my_easy_dict = class_sample.SampleEasyDict('brian')

    print my_easy_dict['name']
    print my_easy_dict

    print 'The name is: %(name)s' % my_easy_dict

    print 'Keys: ', my_easy_dict.keys()
    print 'Values: ', my_easy_dict.values()
    print 'Items: ', my_easy_dict.items()