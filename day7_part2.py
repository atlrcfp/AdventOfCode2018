# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:43:28 2019

@author: AFREEMA3
"""

class worker:
    def __init__(self):
        self.job = ""
        self.busy = False
        self.remaing_duration = 0
        
        
    def take_job(self, task):
        self.job = task
        self.remaing_duration = 60 + ord(task) - 64