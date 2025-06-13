import numpy as np
import math
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Generate Voronoi Diagram
def genVoronoi(points):
    vor = Voronoi(points)

    fig, ax = plt.subplots(figsize = (6,6))
    fig = voronoi_plot_2d(vor, show_vertices = False, ax = ax)

    plt.title("Voronoi Diagram")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()


# Generate Data Set
np.random.seed(100)
count = 50
t = np.random.rand(count) * 2 * math.pi
x = (2 + np.cos(3*t)) * np.cos(t)/3 
y = (2 + np.cos(3*t)) * np.sin(t)/3 
points = np.stack((x,y), axis = 1)
genVoronoi(points)

