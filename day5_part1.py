# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:35:57 2019

@author: atlrc
"""

with open('day5.txt', 'r') as file:
    data = list(file.read()) # read the contents of file and put into list for every char
    #print(len(data))
    initial_length = len(data)
    final_length = 1

while initial_length != final_length:
    initial_length = len(data)
    for n in range(len(data)-1):
        if data[n] != data[n+1] and (data[n] == data[n+1].upper() or data[n] == data[n+1].lower() ):
            print(data[n:n+2])
            del data[n:n+2]
            break
    final_length = len(data)
    
print(len(data))