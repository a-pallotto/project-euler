# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:49:41 2018

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

@author: pallo
"""
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

primes = []

for j in range(2,999999):
    if isPrime(j) == True:
        primes.append(j)
    if len(primes)==10001:
        break
print(max(primes))