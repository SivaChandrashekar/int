#!/usr/bin/env python -u
# encoding: utf-8

#https://docs.python.org/2/library/

import cStringIO

output = cStringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line'
contents = output.getvalue()
output.close()
print contents