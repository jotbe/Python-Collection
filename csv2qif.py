#!/bin/env python
#
# csv2qif.py - Convert CSV data to QIF
#
# This script will take a delimiter-separated list
# and converts it to Quicken Interchange Format (QIF).
#
# Author: Jan Beilicke <dev@jotbe-fx.de>
# Date created: 2011-03-20
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
# - TODO: Support ISO 8859-15 input/output
# - TODO: Code refactoring
#
# == QIF Format ==
# 
# !Type:Bank
# Dmm.dd'YYYY
# U-123.45
# T-123.45
# PPayee
# ^
# Ddd.mm'YYYY
# U-456.78
# T-456.78
# PPayee
# ^
# 
# Note the caret (^) at the end of each entry
# 
# For explanation see:
# http://en.wikipedia.org/wiki/Quicken_Interchange_Format
# 
# More in-depth information:
# http://svn.gnucash.org/trac/browser/gnucash/trunk/src/import-export/qif-import/file-format.txt
#

import argparse
import csv
import datetime
from decimal import *

# Parse args from command-line
parser = argparse.ArgumentParser(description='Convert a Comma-Separated Value (CSV) to Quicken Interchange Format (QIF)')

parser.add_argument('-i', '--ignore-lines', metavar='LINES', default=1,
                    help='CSV: Header lines to ignore (default: %(default)r)')
parser.add_argument('-d', '--delim', metavar='DELIM', default=';',
                    help='CSV: Records delimiter (default: %(default)r)')
parser.add_argument('-q', '--quote-char', metavar='QC', default='"',
                    help='CSV: Character for quoting strings (default: %(default)r)')
parser.add_argument('--decimal-mark', metavar='MARK', default=',',
                    help='CSV: Decimal mark (default: %(default)r)')
parser.add_argument('--thousands-sep', metavar='DELIM', default='.',
                    help='CSV: Thousands separator (default: %(default)r)')
parser.add_argument('--col-date', metavar='N', type=int, default=1,
                    help='CSV: Index of column booking-date (default: %(default)r)')
parser.add_argument('--col-payee', metavar='N', type=int, default=3,
                    help='CSV: Index of column payee (default: %(default)r)')
parser.add_argument('--col-amount', metavar='N', type=int, default=19,
                    help='CSV: Index of column amount (default: %(default)r)')
parser.add_argument('input', metavar='CSVFILE', type=file,
                   help='Source file: /path/to/file.csv')
parser.add_argument('output', metavar='QIFFILE', type=argparse.FileType('w'),
                   help='Target file: /path/to/file.qif')

args = parser.parse_args()


# CSV input
inputFile = args.input
# Ignore header lines
skipLines = args.ignore_lines
# Delimiter
delim = args.delim
# Quote character
quoteChar = args.quote_char
# Decimal separator
# For input we will not rely on any locales
decMark = args.decimal_mark
# Thousands separator
thousandsSep = args.thousands_sep
# Data type
qDataType = 'Bank'
# QIF account name (not used right now)
qAccName = 'Girokonto'
# QIF account type (not used right now)
qAccType = 'Cash'
# Column key (int) for the QIF date
qDate = args.col_date
# Column key (int) for the QIF payee
qPayee = args.col_payee
# Column key (int) for the QIF amount
qAmount = args.col_amount
# QIF output
outputFile = args.output
# QIF header
qifHdr = '''!Type:{type}
'''.format(type=qDataType)
# QIF template
qifTpl = '''D{date}
U{amount}
T{amount}
P{payee}
^
'''

# Main program
print '''
Input: %(in)s
Output: %(out)s

-> Converting to QIF''' % {'in': inputFile.name, 'out': outputFile.name}

csvReader = csv.reader(inputFile, delimiter = delim, quotechar = quoteChar)
qifWriter = outputFile

# Write header
qifWriter.write(qifHdr.format(accname = qAccName, acctype = qAccType))

# Set decimal precision
getcontext().prec = 2

for row in csvReader:
    if csvReader.line_num <= skipLines:
        continue

    # Convert date
    d = row[qDate].split('.')
    d = datetime.date(int(d[2]), int(d[1]), int(d[0]))
    date = d.strftime('%m.%d\'%Y')

    # Convert amount to decimal
    amount = Decimal(row[qAmount].replace(thousandsSep, '').replace(decMark, '.'))

    # Create qif entry
    entry = qifTpl.format(date = date, amount = amount, payee = row[qPayee])

    qifWriter.write(entry)

qifWriter.close()

print 'Done.'