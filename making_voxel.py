# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 19:26:28 2022

@author: user
"""

'''
point cloud 내에서 팔진트리 생성 시도
한 점을 중심으로 해서 팔분공간을 생성해서 값을 비교함.
'''

import random

# Vertex는 클래스로 정의.

def find_center(input_list):
    # 자식클래스 생성시점에서 오류발생
    if len(input_list) == 0:
        return None
    elif len(input_list) == 1:
        return (input_list[0])
    
    x_list = sorted(input_list, key = lambda x : x[0])
    y_list = sorted(input_list, key = lambda x : x[1])
    z_list = sorted(input_list, key = lambda x : x[2])
    
    min_p = (x_list[0][0], y_list[0][1], z_list[0][2])
    max_p = (x_list[-1][0], y_list[-1][1], z_list[-1][2])
    
    print(((min_p[0] + max_p[0])/2, (min_p[1] + max_p[1])/2, (min_p[2] + max_p[2])/2))
    
    return ((min_p[0] + max_p[0])/2, (min_p[1] + max_p[1])/2, (min_p[2] + max_p[2])/2)


class Octree():
    # 중심점과 포인트리스트 삽입
    def __init__(self, point, point_list):
        self.pt_x = point[0]
        self.pt_y = point[1]
        self.pt_z = point[2]
        self.this_list = point_list
        self.area = [[] for i in range(8)]
        
        # print(self.this_list)
        
        for i in self.this_list:
            self.insert(i)
        
        print(self.area)
        
        self.child_list = []
        
        # self.make_child()
        
    # 좌표 값에 따라서 팔분공간에 점을 분류하는 과정
    def insert(self, point):
        if point[0] >= self.pt_x and point[1] >= self.pt_x and point[2] >= self.pt_z:
            self.area[0].append(point)
        elif point[0] >= self.pt_x and point[1] >= self.pt_x and point[2] <= self.pt_z:
            self.area[1].append(point)
        elif point[0] >= self.pt_x and point[1] <= self.pt_x and point[2] >= self.pt_z:
            self.area[2].append(point)
        elif point[0] >= self.pt_x and point[1] <= self.pt_x and point[2] <= self.pt_z:
            self.area[3].append(point)
        elif point[0] <= self.pt_x and point[1] >= self.pt_x and point[2] >= self.pt_z:
            self.area[4].append(point)
        elif point[0] <= self.pt_x and point[1] >= self.pt_x and point[2] <= self.pt_z:
            self.area[5].append(point)
        elif point[0] <= self.pt_x and point[1] <= self.pt_x and point[2] >= self.pt_z:
            self.area[6].append(point)
        elif point[0] <= self.pt_x and point[1] <= self.pt_x and point[2] <= self.pt_z:
            self.area[7].append(point)
    
    # 자식 옥트리 만들기
    def make_child(self):
        for i in self.area:
            self.child_list.append(Octree(find_center(i), i))
        
        print(self.child_list)


point_list = []
for i in range(50):
    x = random.randint(0, 101)
    y = random.randint(0, 101)
    z = random.randint(0, 101)
    point_list.append((x, y, z))



Octree_1 = Octree(find_center(point_list), point_list)
Octree_1_1 = Octree(find_center(Octree_1.area[0]), Octree_1.area[0])