# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:36:21 2019

@author: atlrc
"""
import re
unsorted = []

with open('day4.txt', 'r') as file:
    for line in file:
        unsorted.append(re.split('\[|\] |#| begins', line)) #load each line into list and split
    
sorted_list = sorted(unsorted) # sort the list of lists by time
guard_dictionary = {}   #initialise a dictionary of dictionaries

for item in sorted_list:
   
    if item[2] == "Guard ":
        if item[3] not in guard_dictionary: # if not there, add
            guard_dictionary[item[3]]={} # with key equal to the ID
            for x in range(60):         # create minute entries
                guard_dictionary[item[3]]["min{0}".format(x)]=0
        current_guard =  item[3]        # record the current guard
 
    if item[2].startswith("falls asleep"):
        fall_asleep_time = item[1][-2:] #grab the minute they fall asleep
   
    if item[2].startswith("wakes up"):
        for minute in range(int(fall_asleep_time),int(item[1][-2:])):
            guard_dictionary[current_guard]["min{0}".format(minute)] += 1 #increment that minute asleep    

total_mins = {}
most_often_min = {}

for guardID in guard_dictionary:
    guard_dictionary[guardID]["total"] = 0
    guard_dictionary[guardID]["best_min"] = 0
    guard_dictionary[guardID]["best_min"] = max(guard_dictionary[guardID], key=guard_dictionary[guardID].get)
    for minute in guard_dictionary[guardID]:
        if minute != "best_min": 
            guard_dictionary[guardID]["total"] = guard_dictionary[guardID]["total"] + guard_dictionary[guardID][minute]
            
    total_mins[guardID] = guard_dictionary[guardID]["total"]
    most_often_min[guardID] = guard_dictionary[guardID][guard_dictionary[guardID]["best_min"]]
    
most_sleepy_guard = max(total_mins, key = total_mins.get)
most_reliable_guard = max(most_often_min, key = most_often_min.get)

print("The most sleepy guard is", most_sleepy_guard, "with a total of ", guard_dictionary[most_sleepy_guard]["total"], "minutes asleep.")
print("Guard", most_sleepy_guard, "slept most at time: 00:", guard_dictionary[most_sleepy_guard]["best_min"][3:])
print("Therefore,", int(most_sleepy_guard)*int(guard_dictionary[most_sleepy_guard]["best_min"][3:]))

print("Guard", most_reliable_guard, "is the most consistent, most often sleeping in minute,", guard_dictionary[most_reliable_guard]["best_min"][-2:])
print("Therefore,", int(most_reliable_guard)*int(guard_dictionary[most_reliable_guard]["best_min"][-2:]))