#!/usr/bin/env python

"""Sample instantiation of db class

This script is just a sample for dealing with a database in Python

== Prerequisites ==

The following commands are executed using the MySQL console.

- Create a new database 'pytest':
mysql> CREATE DATABASE pytest;

- Create a test user 'pyuser':
mysql> CREATE USER 'pyuser'@'localhost' IDENTIFIED by 'pyt3ster';

- Grant rights to user:
mysql> GRANT ALL ON pytest.* TO 'pyuser'@'localhost';

For creating and populating the demo table, one should run `mysql-sample`.

TODO: Put the connect() code into a new class or maybe into GeneralDBCmd (refactor name!)

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2011-04-01'

import MySQLdb as mdb
from mysqldb_class_sample import GeneralDBCmd

if __name__ == '__main__':
    dbhost = '127.0.0.1'
    dbuser = 'pyuser'
    dbpwd = 'pyt3ster'
    db = 'pytest'
    tbl = 'tbl_test'

    c = mdb.connect(dbhost, dbuser, dbpwd, db)

    q = GeneralDBCmd(c, tbl)
    q.debug = True
    
    print dir(q)
    print 'MySQL-Version: %s' % q.get_mysql_version()

    print 'Querying field 1 of row 1 \'q[1][1]\': ', q[1][1]

    for x in xrange(0,2):
        print 'Name (range) #%s: %s' % (x, q[x][1])
    
    for x in q:
        print 'Name: %s' % (x[1],)
