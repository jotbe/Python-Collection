#!/usr/bin/env python

"""Simple script for checking an URL for specific changes.

When a string is found in the website, referenced by the URL,
a notification will be sent by mail.
The site-check will then be disabled. If you want to activate
it again, just remove the corresponding logfile.

"""
__author__ = 'Jan Beilicke <dev@jotbe-fx.de>'
__date__ = '2012-04-30'

import urllib2
import smtplib
import re
from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    update_logfile = 'site-check.log'
    url = 'http://blog.jotbe-fx.de'
    search_str = 'privacy'

    send_mail = False
    smtp_server = 'localhost'
    smtp_from = 'me@example.org'
    smtp_to = ['you@example.org', 'another@example.org']
    smtp_subject = 'Site has changed! :)'

    today = datetime.utcnow()
    last_date = today - timedelta(1)

    extracted_date = ""
    already_checked_ok = False

    try:
        ul = open(update_logfile, 'r')
        extracted_date = ul.read(26)
        ul.close()
    except IOError as e:
        if e.errno != 2:  # File not found
            print(e)
            exit(1)

    if extracted_date:
        m = re.match('(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', extracted_date)
        if m:
            last_date = datetime.strptime(m.group(0), '%Y-%m-%d %H:%M:%S')
            already_checked_ok = True

    print 'Last check (UTC):', last_date
    date_diff = abs(today - last_date)

    #if date_diff.days >= 1:
    if not already_checked_ok:

        site = urllib2.urlopen(url)

        if search_str in site.read():
            print('Found!')

            if send_mail:
                smtp_msg = """\
From: {0}
To: {1}
Subject: {2}

Hi!

The following URL has been updated recently ({4} UTC):

{3}

Have a nice day!
""".format(smtp_from, ','.join(smtp_to), smtp_subject, url, last_date)
                s = smtplib.SMTP(smtp_server)
                s.sendmail(smtp_from, smtp_to, smtp_msg)
                s.quit()

            fp = open(update_logfile, 'w')
            fp.write(';'.join([today.strftime('%Y-%m-%d %H:%M:%S'), search_str]))
        else:
            print('Not found')
    else:
        print('Site was already updated. If you want to reset the site-check, \
please delete {0}').format(update_logfile)
