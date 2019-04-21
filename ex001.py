# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:09:19 2018

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

multiples = []                                                       
n=0
while n<999:
    n=n+1
    if n%3==0 or n%5==0:
        multiples.append(n)                 
        
print(sum(multiples))  