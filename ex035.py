# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:19:10 2018

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

@author: pallo
"""
# Rotate numbers
def rotate(s):
    s=str(s)
    return [s[i:]+s[:i] for i in range(len(s))]

# Check if number is prime
def isPrime(k):
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    return True          

#Create list of prime numbers under 1 million
primes = []
for j in range(2,1000000):
    if isPrime(j) is True:
        primes.append(j)

# Create a list of the circular prime numbers. Go through each prime number
# For that number, create a list of rotations. If all the elements of list 
# are prime, then add to list of circular primes.        
circ = []
for num in primes[:]:
    a = rotate(num)
    if all(isPrime(int(a[l])) for l in range(len(a))) is True:
            circ.append(num)
    
print(len(circ))
  