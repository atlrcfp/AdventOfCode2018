# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:08:00 2019

@author: atlrc
"""
double_letters = 0
triple_letters = 0

with open('day2.txt', 'r') as f:
    lines = f.readlines()
    for current_row in range(len(lines)-1):
        current_string = lines[current_row]
        for compare_row in range(current_row,len(lines)-1):
            same_char = 0
            same_string = []
            compare_string = lines[compare_row]
            for char in range(len(lines[current_row])):
                if current_string[char] == compare_string[char]:
                    same_char +=1
                    same_string += current_string[char]
            #print(same_char)
            if same_char == len(lines[current_row]) - 1:
                str1 = "".join(same_string)
                print(str1)
        #print("Current row:", current_row)
    
#    for line in f:
#        
#        for letter in line:
#            
#            for char in line:
#                if letter == char:
#                
#print("Number of boxes with triple letters:", triple_letters)
#print("Number of boxes with double letters:", double_letters)                     
#print("Checksum is therefore", triple_letters*double_letters)   