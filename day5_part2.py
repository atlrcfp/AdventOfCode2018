# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:35:57 2019

@author: atlrc
"""

import string

def remove_elements(x, l):
    for _ in range(l.count(x)):
        l.remove(x)

def react_polymer(data):
    initial_length = len(data)
    final_length = 1
    while initial_length != final_length:
        initial_length = len(data)
        for n in range(len(data)-1):
            if data[n] != data[n+1] and (data[n] == data[n+1].upper() or data[n] == data[n+1].lower() ):
                #print(data[n:n+2])
                del data[n:n+2]
                break
        final_length = len(data)
     
with open('day5.txt', 'r') as file:
    data = list(file.read())

resultant_length = len(data) #starting length

for char in string.ascii_lowercase:
    with open('day5.txt', 'r') as file:
        data = list(file.read()) # read the contents of file and put into list for every char
   
    remove_elements(char,data)
    remove_elements(char.upper(),data)
    print("Removed", char, "and", char.upper())
    react_polymer(data)
    
    if len(data) < resultant_length:
        resultant_length = len(data)
        best_char = char        

print(resultant_length)
print(char)