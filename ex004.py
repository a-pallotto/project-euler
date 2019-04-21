# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 18:44:58 2018

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

@author: pallo
"""

p=[]
for a in range(999, 1, -1):
    for b in range(a ,1 , -1):
        x=a*b
        s=str(x)
        if s[::-1]==s[::]:
            p.append(x)

print(max(p))

factors=[]
n=max(p)
i=1
for i in range(1,n):
    if n%i==0:
        factors.append(i)
        
