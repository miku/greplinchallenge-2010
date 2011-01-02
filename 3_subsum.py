#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

# l = (1, 2, 3, 4, 6)
l = (3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99)

counter = 0

for r in range(2, len(l) + 1):
    for subset in itertools.combinations(l, r=r):
        if subset[-1] == sum(subset[:-1]):
            counter += 1
            print subset

print "Password level 3:", counter
