# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:24:12 2019

@author: afreema3
"""

import re

with open('day3.txt', 'r') as file:
    for line in file: #line = file.readline()
        elements = re.split(' |,|: |x|\n', line)
        x = int(elements[2]) #x starting co-ord, from left
        y = int(elements[3]) #y starting co-rd, from top
        width = int(elements[4]) #width of section
        height = int(elements[5]) #height of section
        
        
    
    