#!/usr/bin/env python
import sys

#find the file name form agrument
file_name=sys.argv[1]

#open the file
file=open(file_name)

#read lines one by one and do somethign witht htem:
for line in file.readlines():
	print line



