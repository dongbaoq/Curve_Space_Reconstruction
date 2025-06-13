import numpy as np
import math
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

MAX = 100

def dist(p, q):
    return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

def ishalf(p, q, r):
    if((p[0] - q[0]) * (p[0] - r[0]) + (p[1] - q[1]) * (p[1] - r[1]) < 0):
        return 1
    else:
        return 0

# NN-CRUST algorithm computes Curve Reconstruction
def NN_CRUST(points):
    vor = Voronoi(points)
    ridge = vor.ridge_points
    E = []
    shortdist = np.ones(points.shape[0]) * MAX
    shortind = np.zeros(points.shape[0], dtype = int)

    for pq in ridge:
        d = dist(points[pq[0]], points[pq[1]])
        if(shortdist[pq[0]] > d):
            shortdist[pq[0]] = d
            shortind[pq[0]] = pq[1]
        if(shortdist[pq[1]] > d):
            shortdist[pq[1]] = d
            shortind[pq[1]] = pq[0]
    
    for i in range(points.shape[0]):
        E.append([i, shortind[i]])

    halfdist = np.ones(points.shape[0]) * MAX
    halfind = np.zeros(points.shape[0], dtype = int)

    for pq in ridge:
        d = dist(points[pq[0]], points[pq[1]])
        if(ishalf(points[pq[0]], points[shortind[pq[0]]], points[pq[1]])):
            if(halfdist[pq[0]] > d):
                halfdist[pq[0]] = d
                halfind[pq[0]] = pq[1]
        if(ishalf(points[pq[1]], points[shortind[pq[1]]], points[pq[0]])):
            if(halfdist[pq[1]] > d):
                halfdist[pq[1]] = d
                halfind[pq[1]] = pq[0]
    
    for i in range(points.shape[0]):
        E.append([i, halfind[i]])

    return E

def NN_CRUST_plot_2d(points):
    E = NN_CRUST(points)
    fig, ax = plt.subplots(figsize = (6,6))
    
    for e in E:
        plt.plot((points[e[0]][0], points[e[1]][0]), (points[e[0]][1], points[e[1]][1]), color = "darkblue", markersize = 1)
    plt.scatter(points[:,0], points[:,1], c = "black", marker = 'o', s = 10)
    plt.title("NN_CRUST Algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

# Generate Data Set
np.random.seed(100)
count = 200
t = np.random.rand(count) * 2 * math.pi
x = (2 + np.cos(3*t)) * np.cos(t)/3 
y = (2 + np.cos(3*t)) * np.sin(t)/3 
points = np.stack((x,y), axis = 1)

NN_CRUST_plot_2d(points)

    



    

    