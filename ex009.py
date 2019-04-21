# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:56:01 2018

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

@author: pallo

"""
import time
 
start = time.time()


for a in range(2,500):
    for b in range(a,500):        
        for c in range(b,500):
            if c**2 == a**2+b**2 and a+b+c ==1000:
                print(a,b,c)
                print(a*b*c)
                break
                
elapsed = (time.time() - start)

print("Time elapsed" ,elapsed)    
