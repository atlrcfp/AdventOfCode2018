# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:30:39 2019

@author: AFREEMA3
"""

instruct = []

with open('day7.txt', 'r') as file:
    for line in file:
        instruct.append(line.split(' '))
        
for line in instruct:
    del line[0], line[1:6], line[2:]
    
    
sorted_instruct = sorted(instruct, key = lambda x: x[1])