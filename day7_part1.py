# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:30:39 2019

@author: AFREEMA3
"""
#def add_in_alpha(stringy, char):
#    i = 0
#    while char > string[i]:
#        i += 1
#    stringy.insert(i,char)
#    return string    
        
instruct = []
available = []
pre_req = []
instructions = {}
order = []


with open('day7.txt', 'r') as file:
    for line in file:
        instruct.append(line.split(' '))
        
for line in instruct:
    del line[0], line[1:6], line[2:]
    
#not actually used, but for sanity    
sorted_instruct0 = sorted(instruct, key = lambda x: x[0])
sorted_instruct1 = sorted(instruct, key = lambda x: x[1])

letters = []
for line in instruct:
    if line[0] not in letters:
        letters.append(line[0])
    if line[1] not in letters:
        letters.append(line[1])
        
for letter in letters:
    instructions[letter] = []

for line in instruct:
    instructions[line[1]].append(line[0])
    
#print(instructions)
while len(order) < len(letters):
    for step in instructions:
        try:
            if instructions[step] == [] and step not in available and step not in order:
                available.append(step)
            if set(instructions[step]).issubset(order) and step not in available and step not in order:
                available.append(step)
        except KeyError:
            pass

    available.sort()
    if len(available) > 0:
        order.append(available[0])  
        instructions[available[0]] = "NULL"   
        del available[0]
     
print("".join(order))   


#while len(instruct) > 0:
#    #print("Order:",order)
#    #print("Available:", available)
#    #get the first instruction step in order
##    if len(order) == 0:
#    current_step = instruct[0][0]
#    order.append(current_step)
#      
#    #find all the steps that are now available   
#    for n in range(len(instruct)):
#        #current_step = instruct[n][1]
#        try:
#            #check if already accounted for
#            if instruct[n][1] not in available:
#                #if found, see if it has other prerequisities
#                for i in range(len(instruct)):
#                    if instruct[i][1] == instruct[n][1]:
#                        pre_req.append(instruct[i][0])
#                
#                # if all pre_reqs have already been done, add to available list
#                if set(pre_req).issubset(order):
#                    available.append(instruct[n][1])
#                    #remove all the entries for that pre-req from the instructions                            
#                    for item in pre_req:
#                        for j in range(len(instruct)):
#                            if instruct[j][0] == item and instruct[j][1] == instruct[n][1]:
#                                del instruct[j]
#                #reset the pre-requisities list
#                print("Pre_req", pre_req)
#                print("Order:", order)
#                pre_req = []
#                
#        except IndexError:
#            pass
#
#    available.sort()
#    print("Available",available)
#    
#    if len(available) > 0:
#        current_step = available[0]
#        order.append(current_step)  
#        del available[0]
#   
#    print("Order:", order)
#          
#
#    print("Available",available)
#print("".join(order))


