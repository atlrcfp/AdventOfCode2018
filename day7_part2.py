# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:43:28 2019

@author: AFREEMA3
"""
#initialise time
t = 0

#define worker class
class worker:
    def __init__(self):
        self.job = ""
        self.busy = False
        self.remaining_time = 0
        
    def take_job(self, task):
        if self.busy == False:
            self.job = task
            #print(self.job)
        else:
            return "Already busy"
        self.remaining_time = 60 + ord(task) - 64
        self.busy = True
        
    def update(self):
        #print(self.remaining_time)
        if self.remaining_time > 0:
            self.remaining_time = self.remaining_time - 1
            if self.remaining_time == 0:    #just completed that job
                self.busy = False
                #return the job just completed
                return self.job
        else:           
            return None    #not working on a job
        
        
#define arrays for sorting instructions etc
instruct = []
available = []
pre_req = []
instructions = {}
complete = []

#create the workers
workers = [worker() for i in range(5)]

def find_available_worker(workers):
    for worker in workers:
        if worker.busy == False:
            return worker
            break
    return -1           #if no workers are available

def update_workers(workers):
    just_completed = []
    for worker in workers:
        status = worker.update()    #call update function just once
        if status != None:
            just_completed.append(status)
#   if len(completed) != 0:
    return just_completed
    
    
    
    
with open('day7.txt', 'r') as file:
    for line in file:
        instruct.append(line.split(' '))
        
for line in instruct:
    del line[0], line[1:6], line[2:]
    
#not actually used, but for sanity    
sorted_instruct0 = sorted(instruct, key = lambda x: x[0])
sorted_instruct1 = sorted(instruct, key = lambda x: x[1])

# create dictionary of tasks and pre-requisits
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
    
    
while len(complete) < len(letters):
    for step in instructions: #step is the key in the dict, i.e. the letter.
        try:
            if (len(instructions[step]) == 0 or set(instructions[step]).issubset(complete)) and (step not in available) and (step not in complete): #create set out of pre-requisits and see if is a subset of complete
                available.append(step) 

        except KeyError:
            pass

    available.sort()
    #assign 
    while len(available) > 0:
        if find_available_worker(workers) == -1:
            break #if none available
        else:
            find_available_worker(workers).take_job(available[0])
            instructions[available[0]] = ["0"]   
            del available[0]
    
    #update all workers, find any completed, and add those to complete
    just_completed = update_workers(workers) 
    if len(just_completed) != 0:
        complete.append("".join(just_completed)) 
    t = t+1
    
    
print(complete)
print(t)
