# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:38:02 2018

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
 and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.

@author: pallo
"""
#find the square of the sum
numbers=[]
for i in range(1,101):
    numbers.append(i)
    
ssum=sum(numbers)
squareofsum= ssum*ssum


#find the sum of squares
numbers2=[]
for j in range(1,101):
    k=j*j
    numbers2.append(k)
sumofsquares=sum(numbers2)


#Find the difference
difference = squareofsum - sumofsquares
print(difference)
