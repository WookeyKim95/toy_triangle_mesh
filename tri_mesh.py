# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:11:54 2022

@author: blueb
"""

import random
import math

def binary_search(list_input, value):
    medium = len(list_input) // 2
    
    if list_input[medium] == value:
        return True
    
    else:
        if len(list_input) <= 1:
            return False
        if binary_search(list_input[medium:], value):
            return True
        else:
            return binary_search(list_input[:medium], value)

class Mesh():
    def __init__(self):
        self.Verticies = []
        return
    
    def insert_triangle(self, a):
        self.Verticies.append(a)
        return

# Vertex는 클래스로 정의.
class Vertex():
    def __init__(self, xyz, value):
        self.pos_xyz = xyz
        self.neighbor_1 = None
        self.neighbor_2 = None
        self.max_length = value
        return
    
    # 점과 가장 가까운 두 점을 구하는 과정
    def cal_distance(self, list_input, i):
        point_x, point_y = i[0], i[1]
        
        dis_point_list = []
        
        ## x, y 좌표를 찾아서 max_length 밖에 있는 점들을 걸러내는 과정
        for k in range(list_input.index(i), -1, -1):
            if abs(point_x - list_input[k][0]) > self.max_length:
                left_index = k
        
        for l in range(list_input.index(i), len(list_input)):
            if abs(point_y - list_input[l][0]) > self.max_length:
                right_index = l
        
        ## 계산할 것만 거리 계산을 진행한다.
        list_to_cal = list_input[left_index:right_index+1]
        
        for j in list_to_cal:
            if abs(point_x - j[0]) > self.max_length or abs(point_y - j[1]) > self.max_length:
                continue    
            
            else:
                distance = math.sqrt((j[0]-point_x)**2 + (j[1]-point_y)**2)
                dis_point_list.append((distance, j))
            
        dis_point_list = sorted(dis_point_list, key = lambda x : (x[0]), reverse=True)
        
        return dis_point_list
    
    def return_Vertex(self):
        return (self.pos_xyz[0], self.pos_xyz[1], self.pos_xyz[2])
    
    # 가장 가까이 있는 세 점을 연결하는 과정
    def connect_line(self, vertex, list_input):
        dis_point_list = self.cal_distance(list_input)
        print(dis_point_list)
        if self.neighbor_1 == None:
            self.neighbor_1 = dis_point_list.pop(0)[1]
        if self.neighbor_2 == None and self.neightbor_1 != None:
            self.neighbor_2 = dis_point_list.pop(0)[1]
        

class line():
    def __init__(self, V1, V2):
        self.V1 = V1
        self.V2 = V2

class Triangle():
    def __init__(self, V1=None, V2=None, V3=None):
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
    
class Verticies():
    def __init__(self, value):
        self.Vertex_list = []
        self.max_length = value
    
    def add_Vertex(self, input_point):
        self.Vertex_list.append(input_point)
        
    def show_list(self):
        for i in self.Vertex_list:
            print(i.return_Vertex())
    
    
Mesh1 = Mesh()
Verticies_class = Verticies(8)

for i in range(50):
    a, b, c = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 10)
    adding_point = Vertex((a, b, c), 8)
    Verticies_class.add_Vertex(adding_point)
'''
Verticies_class.Vertex_list = sorted(Verticies_class.Vertex_list, key = lambda x : (x[0]))

max_distance = 8
'''
Verticies_class.show_list()
