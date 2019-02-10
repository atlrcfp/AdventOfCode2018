# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:35:57 2019

@author: atlrc
"""
import numpy as np

coords = []

def manhattan(x1,y1,x2,y2):
    return (abs(x1-x2)+abs(y1-y2))


     
with open('day6.txt', 'r') as file:
    for coord in file:
        coords.append(coord.split(','))

coords = [[int(float(j)) for j in i] for i in coords]     
        
width = max([sublist[0] for sublist in coords])
height = max([sublist[1] for sublist in coords])


grid = np.zeros([height+1,width+1])

for x in range(len(coords)):
    grid[coords[x][1],coords[x][0]] = x+1

for i in range(width+1):            # go over every element in the grid
    for j in range(height+1):
        distance = []
        for x in range(len(coords)): # and calculate the distance to every co-ordinate
            distance.append(manhattan(i,j,coords[x][0],coords[x][1]))
        
        if distance.count(min(distance)) == 1: # if there's only one closest
            grid[j,i] = distance.index(min(distance)) # populate that space with its reference
        else:                                   #if tied distances, put 0
            grid[j,i] = 0
sizes = []

for x in range(1,len(coords)+1):
    sizes.append(np.count_nonzero(grid == x))

boundary = []

for i in range(width+1):
    if grid[0,i] not in boundary:
        boundary.append(grid[0,i])
        
for i in range(width+1):
    if grid[height,i] not in boundary:
        boundary.append(grid[height,i])
        
for i in range(height+1):
    if grid[i,0] not in boundary:
        boundary.append(grid[i,0])
        
for i in range(height+1):
    if grid[i,width] not in boundary:
        boundary.append(grid[i,width])
        
for location in boundary:
    sizes[int(location-1)] = 0


print(max(sizes))