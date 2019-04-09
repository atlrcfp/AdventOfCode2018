# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:34:38 2019

@author: AFREEMA3
"""


class node:
    def __init__(self,num_children,num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.children = [node(0,1) for i in range(self.num_children)]
        
    #def reproduce(self):
        #children = [node() for i in range(self.num_children)]
        
    def get_meta(data):
        return 1
    
with open('day8.txt', 'r') as file:
    data = file.read()
    
data = data.split(" ")


node_a = node(2,3)

nodes = [node_a]