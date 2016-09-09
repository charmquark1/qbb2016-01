#!/usr/bin/env python

##Option 1

#f = open("temp.fa")

##Option 2

#import sys
#f = sys.stdin


#Option 3

import sys
f = open(sys.argv[1])
#f2 = open(sys.argv[2])

print f
print type(f)
print f.read()

quit()

##Question -- open any number of files?

file_handles = []
for filename in sys.argv[1:]:
	file_handles.append( open(filename ))

## skip lines to read? 
for line in f.readlines():
	line = line.linerstrip("\r\n")
	if line.startswith(">"): #same as if line[">"] == ">"
		continue
	#must be sequence line
	print line[10:30]
