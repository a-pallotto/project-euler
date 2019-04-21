# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:51:08 2018

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

@author: pallo
"""
# Function that calculates sum of proper divisors
def divsum(n):
    d=[]
    for i in range(1,n):
        if n%i==0:
            d.append(i)
    return sum(d)
        
amiclist = []

for j in range(1,10000):
    k = divsum(j)  
    f = divsum(k)
    if (j==f) and (j!=k):
        amiclist.append(j)
        amiclist.append(f)

amicablelist = []
for m in amiclist[:]:
    if m not in amicablelist:
        amicablelist.append(m)
    
print(sum(amicablelist))