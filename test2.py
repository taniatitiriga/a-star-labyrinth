from mazelib import Maze
from mazelib.generate.Prims import Prims
import matplotlib.pyplot as plt

def showPNG(grid):
    """Generate a simple image of the maze."""
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap="gray", interpolation="nearest")
    plt.xticks([]), plt.yticks([])
    plt.show()

m = Maze()
m.generator = Prims(10, 10)

showPNG(m.generate())