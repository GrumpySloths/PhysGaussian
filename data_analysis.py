from plyfile import PlyData, PlyElement
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def info_ply(ply_path):
    ply_data=PlyData.read(ply_path)
    # print("header for ply data:")
    # print(ply_data.header)
    xyz = np.stack((np.asarray(ply_data.elements[0]["x"]),
                np.asarray(ply_data.elements[0]["y"]),
                np.asarray(ply_data.elements[0]["z"])),  axis=1)
    print("xyz shape:",xyz.shape)
    print("max point:",xyz.max(axis=0))
    print("min point:",xyz.min(axis=0))

    return xyz

def print_header(ply_path):
    ply_data=PlyData.read(ply_path)
    print("header for ply data:")
    print(ply_data.header)

    return ply_data.header

if __name__ == "__main__":

    data_path="./log_paladin/init_particles.ply"
    
    print_header(data_path)    

    print("info for origin data:")
    data_xyz=info_ply(data_path)
    transformed_data_path="./log_paladin/transformed_particles.ply"
    print("info for transformed  data:")
    transformed_data_xyz=info_ply(transformed_data_path)


    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 根据 x, y, z 值设置颜色
    colors = np.where((0.5 < transformed_data_xyz[:, 0]) & (transformed_data_xyz[:, 0] < 1.5) &
                    (0.5 < transformed_data_xyz[:, 1]) & (transformed_data_xyz[:, 1] < 1.5) &
                    (0.22 < transformed_data_xyz[:, 2]) & (transformed_data_xyz[:, 2] < 0.78), 'r', 'b')

    ax.scatter(transformed_data_xyz[:, 0], transformed_data_xyz[:, 1], transformed_data_xyz[:, 2], s=0.3,c=colors, marker='o')

    ax.set_title('3D Visualization of data_xyz')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    #将图片保存到"./log_paladin/3d_visualization.png"
    plt.savefig("./log_paladin/3d_visualization.png")
    