#!/bin/env python
#
# csv2qif.py - Convert CSV data to QIF
#
# This script will take a delimiter-separated list
# and converts it to Quicken Interchange Format (QIF).
#
# == Use case == 
#
# Export a bank statement as CSV, convert it to QIF
# and import it into an accounting software like
# eg. GnuCash.
#
# == Caveats and Todos ==
# 
# - FIXME: Only date (D), payee (P) and amount (U, T) are currently supported
# - FIXME: Only german date format supported
# - TODO: Support CLI arguments
# - TODO: Code refactoring
#
# Author: Jan Beilicke <dev@jotbe-fx.de>
# Date created: 2011-03-20
#

import csv
import datetime

# CSV input
inputFile = 'statements-utf-8.csv'
# Ignore header lines
skipLines = 1
# Delimiter
delim = ';'
# Quote character
quoteChar = '"'
# Column key (int) for the qif date
qDate = 1
# Column key (int) for the qif payee
qPayee = 3
# Column key (int) for the qif amount
qAmount = 19
# Qif output
outputFile = 'statements.qif'

csvReader = csv.reader(open(inputFile,'r'), delimiter=delim, quotechar=quoteChar)

''' Default format for QIF:

!Type:Bank
Dmm.dd'YYYY
U-123.45
T-123.45
PPayee
^
Ddd.mm'YYYY
U-456.78
T-456.78
PPayee
^

Note the caret (^) at the end of each entry

For explanation see:
http://en.wikipedia.org/wiki/Quicken_Interchange_Format

More in-depth information:
http://svn.gnucash.org/trac/browser/gnucash/trunk/src/import-export/qif-import/file-format.txt

'''

qifTpl = '''D{date}
U{amount}
T{amount}
P{payee}
^'''

qifWriter = open(outputFile, 'w')

# Write header
qifWriter.write('''
!Type:Bank
''')

i = 0
for row in csvReader:
	i += 1
	if i <= skipLines:
		continue
	
	# Convert date
	d = row[qDate].split('.')
	d = datetime.date(int(d[2]), int(d[1]), int(d[0]))
	date = d.strftime('%m.%d\'%Y')

	entry = qifTpl.format(date = date, amount = row[qAmount], payee = row[qPayee])
	qifWriter.write(entry)

qifWriter.close()
