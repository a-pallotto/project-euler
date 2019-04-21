# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 08:02:45 2018

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

@author: pallo
"""
a = []
for n in range(100,1000000):
    k = [int(i) for i in str(n)]
    if sum(int(j)**5 for j in k)==n:
        a.append(n)
        
print(sum(a))
    