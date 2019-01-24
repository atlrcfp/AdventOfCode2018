# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:08:00 2019

@author: atlrc
"""
double_letters = 0
triple_letters = 0

with open('day2.txt', 'r') as f:
    for line in f:
        letter2flag = 0
        letter3flag = 0
        for letter in line:
            duplicate_letter_count = 0
            for char in line:
                if letter == char:
                    duplicate_letter_count += 1
            if duplicate_letter_count == 2 and letter2flag == 0:
                double_letters += 1
                letter2flag = 1
            if duplicate_letter_count == 3 and letter3flag == 0:
                triple_letters += 1
                letter3flag = 1
print("Number of boxes with triple letters:", triple_letters)
print("Number of boxes with double letters:", double_letters)                     
print("Checksum is therefore", triple_letters*double_letters)   