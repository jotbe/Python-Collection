#!/usr/bin/env python

"""Sample database class for MySQL

This script is just a sample for dealing with a database class

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2011-04-01'

import MySQLdb as mdb

class GeneralDBCmd:
    
    """Provide general database commands."""
    
    def __init__(self, dbcon, tbl):
        self.dbcon = dbcon
        self.dbcur = self.dbcon.cursor()
        self.tbl = tbl
        self.debug = True
    def __getitem__(self, item):
        self.dbcur.execute('''
            SELECT * FROM %s LIMIT %s, 1;
        ''' % (self.tbl, item))
        return self.dbcur.fetchone()
    def _query(self, q):
        """Display the query in debug mode and execute it."""
        if self.debug: print 'Query: %s' % (q)
        self.dbcur.execute(q)
    def __iter__(self):
        """Create a data set and return an iterator (self)."""
        q ="""
            SELECT * FROM %s
        """% (self.tbl)
        self._query(q)
        # return iterator object with 'next()' method
        return self
    def next(self):
        """Return the next item in dataset or tell Python to stop."""
        r = self.dbcur.fetchone()
        if not r:
            raise StopIteration
        return r
    def get_mysql_version(self):
        """Return the MySQL version of the server."""
        q ="""
            SELECT VERSION();
        """
        self._query(q)
        return self.dbcur.fetchone()
