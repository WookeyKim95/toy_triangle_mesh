# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:06:22 2022

@author: blueb
"""
import random

Vertex_list = []

for i in range(10):
    a, b, c = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 10)
    Vertex_list.append((a, b, c))

print(Vertex_list)



Vertex_sorted_X = sorted(Vertex_list, key = lambda x : (x[0]))
Vertex_sorted_Y = sorted(Vertex_list, key = lambda x : (x[1]))