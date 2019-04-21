# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:46:41 2018

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
@author: pallo
"""
import time
 
start = time.time()

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

primes = []
for j in range(1,2000000,2):
    if isPrime(j) == True:
        primes.append(j)
print(sum(primes)+1)

elapsed = (time.time() - start)

print("Time elapsed" ,elapsed) 