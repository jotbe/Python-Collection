#!/usr/bin/env python
import re

#print '\nPattern matching:'
#m = re.search('(?i)foo', 'blaFoobar')
#print m.group(0)

#print '\nSimple calculation:'
#print '1 + 2 =', 1+2

print '\nLists:'
a = [1,7,4,2,1,5,3]
#for i in a:
#  print i
#print 'end'

a.reverse()
for i in a:
	print i
print '.'

a.sort()
for i in a:
	print i
print '.'

print 'Items before:', len(a)
a.append(9)
print 'Items after:', len(a)

print 'Values within keys 2-5 (excl.):', a[2:5]

print a.pop(1)
print '.'

b=(6,8)
a.extend(b)
a.sort()

for i in a:
	print i
print '.'

print '-----------'
def bla():
	return

foo = bla()

for i in foo:
	print i
print '.'