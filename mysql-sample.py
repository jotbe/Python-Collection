#!/bin/env python
#
# mysql-sample.py - Read from MySQL Database
#
# This script is an example for accessing a MySQL Database
#
# Author: Jan Beilicke <dev@jotbe-fx.de>
# Date created: 2011-03-31
#
# == Use cases ==
#
# - Read some values
#
# == Prerequisites ==
#
# The following commands are executed using the MySQL console.
#
# - Create a new database 'pytest':
# mysql> CREATE DATABASE pytest;
#
# - Create a test user 'pyuser':
# mysql> CREATE USER 'pyuser'@'localhost' IDENTIFIED by 'pyt3ster';
#
# - Grant rights to user:
# mysql> GRANT ALL ON pytest.* TO 'pyuser'@'localhost';
#

import MySQLdb as mdb
import sys

dbhost = '127.0.0.1'
dbuser = 'pyuser'
dbpwd = 'pyt3ster'
db = 'pytest'

# Init connection
try:
    c = mdb.connect(dbhost, dbuser, dbpwd, db)
    cur = c.cursor()
    cur.execute('''SELECT VERSION()''')
    data = cur.fetchone()
    cur.close()
    c.close()
    print 'MySQL-Version: %s' % data
except mdb.Error, e:
    print 'Error %d: %s' % (e.args[0], e.args[1])
    sys.exit()