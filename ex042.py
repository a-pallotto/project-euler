# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 15:23:57 2018

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values
 we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
 If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?

@author: pallo
"""
# Create list of python strings
with open('words.txt') as f:
    words = f.read().split(',')
    words = [list(word.strip('\"')) for word in words]
   

# Create triangle number set for the first 26 numbers
triangles = []
for i in range(1,27):
    t = .5*i*(i+1)
    triangles.append(int(t))

# Make a dictionary to assign numerical values to letters.
numvals = {}
alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for j in alphabet:
    numvals[j] = alphabet.index(j)+1
    
# Create a function to parse through list and add triangle words 
# to list  
triangle_words = []

for word in words:
    if sum([numvals[c] for c in word]) in triangles:
        triangle_words.append(word)

print(len(triangle_words))