# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:17:16 2018
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

@author: pallo
"""
j=1
for i in range(1,101):
    j = i*j
    
print(j)
print("The sum is: ", sum(int(digit) for digit in str(j)))