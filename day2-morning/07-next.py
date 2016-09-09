#! /usr/bin/python

import sys

#suppose, i want to add new column, which is the length

for line in sys.stdin:
	if line.startswith("t_id"):
	print line.rstrip("\r\n")
	continue

	#split foe;s on tab
	fields =line.rstrip("\r\n").split("\t")
	#convert and compute length
	length = int(fields[4]) - int(fields[3])

	#Write out with new field tab separated
	fields.append(str(length))
	print string.join( fields, "\t")


