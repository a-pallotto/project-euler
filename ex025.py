# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:29:11 2018

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
@author: pallo
"""

# Def a fib function
def fib(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a+b, a
        n = n - 1
    return a

# find the index of the first term in the Fibonacci sequence to contain 1000 digits
i=0
while len(str(fib(i)))<1000:
    i = i+1
    
print(i)