import matplotlib.pyplot as plt

def draw_maze(grid):
    """Generate a simple image of the maze."""
    plt.figure(figsize=(10, 5))
    plt.imshow(grid, cmap="gray", interpolation="nearest")
    plt.xticks([]), plt.yticks([])
    plt.show()