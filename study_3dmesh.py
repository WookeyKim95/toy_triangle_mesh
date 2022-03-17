# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:37:01 2022

@author: user
"""

'''
참고 사이트 : https://ichi.pro/ko/python-eulo-pointeu-keullaudeueseo-3d-mesileul-saengseonghaneun-5-dangye-gaideu-60176041760954
'''

import numpy as np
import open3d as o3d

# 포인트 클라우드 파일 열기
input_path="your_path_to_file/"
output_path="your_path_to_output_folder/"
dataname="sample.xyz"
point_cloud= np.loadtxt(input_path+dataname,skiprows=1)

# xyz 파일의 포인트 클라우드 내용 받기
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])

# 포인트 클라우드 시각화
o3d.visualization.draw_geometries([pcd])

#bpa 방법

# 반경매개변수계산
distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 3 * avg_dist

bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))

# 여기의 mesh 자리에다가 파일을 입력할 필요가 있어보임. 오류발생.
dec_mesh = mesh.simplify_quadric_decimation(100000)

dec_mesh.remove_degenerate_triangles()
dec_mesh.remove_duplicated_triangles()
dec_mesh.remove_duplicated_vertices()
dec_mesh.remove_non_manifold_edges()

# 포아송 REstruction
poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8, width=0, scale=1.1, linear_fit=False)[0]

# 표면 필터링
bbox = pcd.get_axis_aligned_bounding_box()
p_mesh_crop = poisson_mesh.crop(bbox)

# ply 파일로 내보내기 (경로입력 필요)
o3d.io.write_triangle_mesh(output_path+"p_mesh_c.ply", p_mesh_crop)


def lod_mesh_export(mesh, lods, extension, path):
    mesh_lods={}
    for i in lods:
        mesh_lod = mesh.simplify_quadric_decimation(i)
        o3d.io.write_triangle_mesh(path+"lod_"+str(i)+extension, mesh_lod)
        mesh_lods[i]=mesh_lod
    print("generation of "+str(i)+" LoD successful")
    return mesh_lods

# bpa 알고리즘 기법 파일 내보내기
my_lods = lod_mesh_export(bpa_mesh, [100000,50000,10000,1000,100], ".ply", output_path)
y_lods2 = lod_mesh_export(bpa_mesh, [8000,800,300], ".ply", output_path)

# 모델 시각화
o3d.visualization.draw_geometries([my_lods[100]])
