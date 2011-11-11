#!/usr/bin/env python

"""Read from MySQL Database

This script is a simple example for accessing a demo MySQL Database

== Use cases ==

- Connect to the MySQL server
- Print the MySQL version of the server
- Drop an existing demo table (should be commented out by default!)
- Create a demo table
- Populate dummy data
- Read dummy data from table

== Prerequisites ==

The following commands are executed using the MySQL console.

- Create a new database 'pytest':
mysql> CREATE DATABASE pytest;

- Create a test user 'pyuser':
mysql> CREATE USER 'pyuser'@'localhost' IDENTIFIED by 'pyt3ster';

- Grant rights to user:
mysql> GRANT ALL ON pytest.* TO 'pyuser'@'localhost';

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2011-03-31'

import MySQLdb as mdb
import sys

if __name__ == '__main__':
    dbhost = '127.0.0.1'
    dbuser = 'pyuser'
    dbpwd = 'pyt3ster'
    db = 'pytest'

    try:
        #c = mdb.connect(dbhost, dbuser, db, read_default_file=os.path.expanduser('~/my.cnf'))
        c = mdb.connect(dbhost, dbuser, dbpwd, db)
        cur = c.cursor()
    except mdb.Error, e:
        print 'Error %d: %s' % (e.args[0], e.args[1])
        sys.exit()

    # Init connection
    def get_mysql_version():
        """Return the MySQL server version."""
        try:
            cur.execute("""SELECT VERSION()""")
            data = cur.fetchone()
            return data
        except mdb.Error, e:
            print 'Error %d: %s' % (e.args[0], e.args[1])
            sys.exit()

    def get_tables():
        """Return a list of database tables."""
        try:
            cur.execute("""SHOW TABLES""")
            data = cur.fetchall()
            return data
        except mdb.Error, e:
            print 'Error %d: %s' % (e.args[0], e.args[1])
            sys.exit()

    def create_demo_table():
        """Create a demo table."""
        try:
            cur.execute("""
                CREATE TABLE tbl_test (
                    test_id INT(11) DEFAULT '0',
                    name VARCHAR(255) DEFAULT '' NOT NULL,
                    PRIMARY KEY (test_id)
                ) ENGINE=InnoDB DEFAULT charset=utf8 COLLATE utf8_general_ci;
            """)
            data = cur.fetchone()
            return data
        except mdb.Error, e:
            print 'Error %d: %s' % (e.args[0], e.args[1])
            sys.exit()

    def populate_demo_table():
        """Populate a demo table with dummy data."""
        try:
            cur.executemany("""
                INSERT INTO tbl_test (test_id, name) VALUES (%s, %s);
            """, [
                (1, 'spam'),
                (2, 'eggs'),
                (3, 'brian'),
            ])
            c.commit()
            return
        except mdb.Error, e:
            c.rollback()
            print 'Error %d: %s' % (e.args[0], e.args[1])
            sys.exit()

    def get_all_demo_data():
        """Select and return all dummy data of the demo table."""
        try:
            cur.execute("""
                SELECT test_id, name FROM tbl_test;
            """)
            data = cur.fetchall()
            return data
        except mdb.Error, e:
            print 'Error %d: %s' % (e.args[0], e.args[1])
            sys.exit()

    def drop_demo_table():
        """Drop the demo table."""
        try:
            cur.execute("""
                DROP TABLE tbl_test;
            """)
            data = cur.fetchall()
            return data
        except mdb.Error, e:
            print 'Error %d: %s' % (e.args[0], e.args[1])
            sys.exit()

    version = get_mysql_version()
    print 'MySQL-Version: %s' % version

    #drop_demo_table()
    create_demo_table()
    tables = get_tables()
    print 'Tables: ', tables

    populate_demo_table()
    data = get_all_demo_data()
    data_names = [row[1] for row in data]
    print 'Names: ', data_names

    cur.close()
    c.close()
