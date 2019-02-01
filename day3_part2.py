# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:24:12 2019

@author: afreema3
"""

import re
import numpy as np

fabric = np.zeros((1000,1000), dtype = np.int8)
intersections = 0
max_width = []
max_height = []
this_one = 0

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
       
print("Fabric marked out")
with open('day3.txt', 'r') as file:    
    for line in file: #line = file.readline()
        elements = re.split(' |,|: |x|\n', line)
        #print(elements)
        x = int(elements[2]) #x starting co-ord, from left
        y = int(elements[3]) #y starting co-rd, from top
        width = int(elements[4]) #width of section
        height = int(elements[5]) #height of section
        
    
        this_one = 1
        
        for i in range(height):
            for j in range(width):
                if fabric[y+i+1,x+j+1] != 1:
                    this_one = 0
        
        if this_one == 1:
            print(elements)
    
    
    