#! /usr/bin/env python

f = open("SRR072893.SAM")

counter = 0

for sun in f.readlines():
	if sun.startswith("@"):
		pass

	else:
		counter = counter + 1


#for sun in f.readlines():
	
#	if sun.startswith("SRR"):
#		counter =+ 1

print counter	

