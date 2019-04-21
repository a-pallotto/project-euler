# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:08:41 2018

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

@author: pallo
"""
checklist=[11 , 12, 13, 14, 15, 16, 17, 18, 19, 20]

# unnecessary to check 1-10

for i in range(2520,999999999,20):
    if all(i % n == 0 for n in checklist):
        print(i)
        break

