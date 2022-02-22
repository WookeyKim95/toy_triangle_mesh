# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:01:35 2022

@author: blueb
"""

import random

class Lag():
    def __init__(self, input_list):
        self.input_list = input_list
    
    def coefficient(self, i, value):
        p = 1
        for x in self.input_list:
            if x[0] == i:
                continue
            p *= (value - x[0])
            p /= (i - x[0])
            
        return p
    
    def cal_lag(self, value):
        val_to_return = 0
        for point in self.input_list:
            val_to_return += self.coefficient(point[0], value) * point[1]
        
        return val_to_return

a_list = []

for i in range(3):
    x, y = random.randint(1,10), random.randint(1,10)
    a_list.append((x, y))

Lag_1 = Lag(a_list)

print(a_list)
print(Lag_1.cal_lag(2))    