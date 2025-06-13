import numpy as np
import math
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# CRUST algorithm computes Curve Reconstruction
def CRUST(points):
    vor = Voronoi(points)
    Union = np.concatenate((points,vor.vertices), axis = 0)
    vor2 = Voronoi(Union)

    E = []
    for ind in vor2.ridge_points:
        if (ind[0] < points.shape[0] and ind[1] < points.shape[0]) :
            E.append([ind[0], ind[1]])
    return E

def CRUST_plot_2d(points):
    E = CRUST(points)
    fig, ax = plt.subplots(figsize = (6,6))
    
    for e in E:
        plt.plot((points[e[0]][0], points[e[1]][0]), (points[e[0]][1], points[e[1]][1]), color = "darkblue", markersize = 1)
    plt.scatter(points[:,0], points[:,1], c = "black", marker = 'o', s = 10)
    plt.title("CRUST Algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

# Generate Data Set
np.random.seed(100)
count = 100
t = np.random.rand(count) * 2 * math.pi
x = (2 + np.cos(3*t)) * np.cos(t)/3 
y = (2 + np.cos(3*t)) * np.sin(t)/3 
points = np.stack((x,y), axis = 1)

CRUST_plot_2d(points)