#!/usr/bin/env python

s = "this is a string"
print "String item six is", s[6]

an_int = 7
i_as_s = str(an_int)
s_as_i = int(7)
a_real = 5.322

s_as_r = float ("5.273673")

for value in (s, an_int, i_as_s, s_as_i):
	print value, type (value)

a_list = [1, 2, 3, 4, 5, 6]
a_tuple = (1,2 , 3, 4, 5, 6)

print a_list, type (a_list)
print a_tuple, type (a_tuple)

a_list[3]=777

my_var_a=[1,2,3,4,5]
my_var_b = my_var_a

my_var_a[2] = 999

print my_var_b
