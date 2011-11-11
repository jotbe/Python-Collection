#!/usr/bin/env python

"""Using class attributes

This script is a sample for accessing and modifying class attributes.

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2011-04-01'

import class_sample

if __name__ == '__main__':
    print dir(class_sample)

    # SampleCounter
    print '\n= SampleCounter ='
    c = class_sample.SampleCounter()

    #print dir(c)
    print 'c.count: ', c.count
    print 'c.instance_count: ', c['instance_count']

    print '-> Creating new instance of SampleCounter:'
    d = class_sample.SampleCounter()

    #print dir(d)
    print 'd.count: ', d.count
    print 'd.instance_count: ', d['instance_count']
    print 'c.count: ', c.count
    print 'c.instance_count: ', c['instance_count']

    print '-> Creating new instance of SampleCounter:'
    e = class_sample.SampleCounter()

    #print dir(e)
    print 'e.count: ', e.count
    print 'e.instance_count: ', e['instance_count']
    print 'd.count: ', d.count
    print 'd.instance_count: ', d['instance_count']
    print 'c.count: ', c.count
    print 'c.instance_count: ', c['instance_count']
