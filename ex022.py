# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:35:00 2018

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

@author: pallo
"""
# Create list with names, and seperate letters
with open('p022_names.txt','r') as f:
    names = f.read().split(',')
    names = sorted(names)
    names = [list(name.strip('\"')) for name in names]
    
# Create dictionary to assign numberical values to alphabet
numvals = {}
alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for j in alphabet:
    numvals[j] = alphabet.index(j)+1

sums = []
i =1
for name in names:
    s = sum([numvals[k] for k in name]) * i
    i=i+1
    sums.append(s)
print(sum(sums))