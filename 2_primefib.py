#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

memo = {0:0, 1:1}

def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def isprime(test):
    if test == 2: return True
    if test < 2 or test % 2 == 0: return False
    return not any(test % i == 0 for i in range(3, int(sqrt(test)) + 1, 2))

def factor(n):
    if n == 1: return [1]
    i = 2
    limit = n**0.5
    while i <= limit:
        if n % i == 0:
            ret = factor(n/i)
            ret.append(i)
            return ret
        i += 1
    return [n]

if __name__ == '__main__':
    constraint = 227000
    for i in range(27, 100):
        if isprime(fib(i)) and fib(i) > constraint:
            # 29 514229
            print i, fib(i)
            break
    print "Password level 2:", sum(factor(fib(i) + 1))
