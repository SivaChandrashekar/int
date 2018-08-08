#!/usr/bin/env python -u
# encoding: utf-8

#https://docs.python.org/2/library/

import cStringIO,csv,sys
csvfilename = "/tmp/1.csv"
output = cStringIO.StringIO()
with open(csvfilename,'w+') as csvfile:
    fieldnames = ['first_name', 'last_name']
    csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerow({'first_name':'siva','last_name':'ram'})
    csvwriter.writerow({'first_name': 'om', 'last_name': 'jai'})
output.write('First line.\n')
print >>output, 'Second line'
contents = output.getvalue()
output.close()
print contents

try:
    with open(csvfilename,"rb") as readcsvfile:
        csv.DictReader(readcsvfile)
        for row in readcsvfile:
            print row
except IOError as e:
    sys.exit('Error reading file - {0} with error {1}'.format(csvfilename,e))
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (csvfilename, readcsvfile.line_num, e))

with open("/tmp/1.txt","w+") as file:
    file.write(contents)
    file.close()

#Python TIPS
'''
1. Classes usage and tips in python
_ underline in the beginning of a method or attribute means you shouldn't access this method
__ you're saying that you don't want anybody to override it, it will be accessible just from inside the own class.
__init__()  is called when the object is created so you can initialize it.
__new__() is called to build the instance
Packages with __init__.py - http://www.reddit.com/r/Python/comments/1bbbwk/whats_your_opinion_on_what_to_include_in_init_py/
'''

#ToDo
'''
Decorators
Flask
'''