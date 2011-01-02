#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The Greplin Programming Challenge
# 	
# 	Level 3
# 	
# 	----------------------------------------
# 
# 	Congratulations.  You have reached the final level.
# 	
# 	For the final task, you must find all subsets of an array
# 	where the largest number is the sum of the remaining numbers.
# 	For example, for an input of:
# 
# 	(1, 2, 3, 4, 6)
# 
# 	the subsets would be
# 
# 	1 + 2 = 3
# 	1 + 3 = 4
# 	2 + 4 = 6
# 	1 + 2 + 3 = 6
# 	
# 	Here is the list of numbers you should run your code on.
# 	The password is the number of subsets.  In the above case the
# 	answer would be 4.
# 	
# 	Enter the password to complete the challenge: 

import itertools

# l = (1, 2, 3, 4, 6)
l = (3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 
	73, 78, 81, 92, 95, 97, 99)

counter = 0

for r in range(2, len(l) + 1):
    for subset in itertools.combinations(l, r=r):
        if subset[-1] == sum(subset[:-1]):
            counter += 1
            # print subset

print "Password level 3:", counter
