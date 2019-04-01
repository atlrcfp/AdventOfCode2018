# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:43:28 2019

@author: AFREEMA3
"""

class worker:
    def __init__(self):
        self.job = ""
        self.busy = False
        self.remaining_time = 0
        
        
    def take_job(self, task):
        self.job = task
        self.remaining_time = 60 + ord(task) - 64
        
    def update(self):
        if self.remaining_time > 0:
            self.remaining_time = self.remaining_time - 1
            
        
worker_a = worker()
worker_b = worker()
worker_c = worker()
worker_d = worker()
worker_e = worker()

worker_a.take_job("X")

print(worker_a.job)
print(worker_a.remaining_duration)