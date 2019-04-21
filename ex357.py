# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:19:10 2018

@author: pallo
"""

# Function to find divisors

def isPrime(k):
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False

    return True          


num = []
div= []
def d(n):
    for i in range(1,n+1):
        if n%i==0:
            if isPrime(i+n/i) is True:
                num.append(n)
            
       
for m in range(100000):
    d(m)
     
           
   
  