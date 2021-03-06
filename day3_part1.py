# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:24:12 2019

@author: afreema3
"""

import re
import numpy as np

fabric = np.zeros((1000,1000), dtype = int)
intersections = 0
max_width = []
max_height = []

with open('day3.txt', 'r') as file:
    for line in file: #line = file.readline()
        elements = re.split(' |,|: |x|\n', line)
        #print(elements)
        x = int(elements[2]) #x starting co-ord, from left
        y = int(elements[3]) #y starting co-rd, from top
        width = int(elements[4]) #width of section
        height = int(elements[5]) #height of section
        max_width.append(x+width)
        max_height.append(y+height)
    
        this_claim = 0
        
        for i in range(height):
            for j in range(width):
                fabric[y+i+1,x+j+1] += 1 #and this_claim == 0:
                    #intersections += 1
                    #this_claim = 1
                    #print(intersections)
        #fabric[y:y+height,x:x+width] = np.ones((height,width), dtype = bool)
    
    for i in range(1000):
            for j in range(1000):
                if fabric[i,j] > 1:
                    intersections += 1
    print("Total number of common squares of fabric:", intersections)
    print("Width of fabric,",max(max_width))
    print("Height of fabric,",max(max_height))
    
    