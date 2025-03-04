from numpy.random import shuffle
import matplotlib.pyplot as plt
from random import randrange
import numpy as np

class Prims():
    """
    The Prims maze-generating algorithm.

    1. Choose an arbitrary cell from the grid, and add it to some
        (initially empty) set visited nodes (V).
    2. Randomly select a wall from the grid that connects a cell in
        V with another cell not in V.
    3. Add that wall to the Minimal Spanning Tree (MST), and the edge's other cell to V.
    4. Repeat steps 2 and 3 until V includes every cell in G.
    """

    def __init__(self, h, w):
        assert w >= 3 and h >= 3, "Mazes cannot be smaller than 3x3."
        self.h = h
        self.w = w
        self.H = (2 * self.h) + 1
        self.W = (2 * self.w) + 1
        
    def _find_neighbors(self, r, c, grid, is_wall=False):
        """Find all the grid neighbors of the current position; visited, or not.

        Args:
            r (int): row of cell of interest
            c (int): column of cell of interest
            grid (np.array): 2D maze grid
            is_wall (bool): Are we looking for neighbors that are walls, or open cells?
        Returns:
            list: all neighboring cells that match our request
        """
        ns = []

        if r > 1 and grid[r - 2][c] == is_wall:
            ns.append((r - 2, c))
        if r < self.H - 2 and grid[r + 2][c] == is_wall:
            ns.append((r + 2, c))
        if c > 1 and grid[r][c - 2] == is_wall:
            ns.append((r, c - 2))
        if c < self.W - 2 and grid[r][c + 2] == is_wall:
            ns.append((r, c + 2))

        shuffle(ns)
        return ns
    
    def generate(self):
        """Highest-level method that implements the maze-generating algorithm.

        Returns
        -------
            np.array: returned matrix
        """
        # create empty grid
        grid = np.empty((self.H, self.W), dtype=np.int8)
        grid.fill(1)

        # choose a random starting position
        current_row = randrange(1, self.H, 2)
        current_col = randrange(1, self.W, 2)
        grid[current_row][current_col] = 0

        # created a weighted list of all vertices connected in the graph
        neighbors = self._find_neighbors(current_row, current_col, grid, True)

        # loop over all current neighbors, until empty
        visited = 1

        while visited < self.h * self.w:
            # find neighbor with lowest weight, make it current
            nn = randrange(len(neighbors))
            current_row, current_col = neighbors[nn]
            visited += 1
            grid[current_row][current_col] = 0
            neighbors = neighbors[:nn] + neighbors[nn + 1 :]
            # connect that neighbor to a random neighbor with grid[posi] == 0
            nearest_n0, nearest_n1 = self._find_neighbors(
                current_row, current_col, grid
            )[0]
            grid[(current_row + nearest_n0) // 2][(current_col + nearest_n1) // 2] = 0

            # find all unvisited neighbors of current, add them to neighbors
            unvisited = self._find_neighbors(current_row, current_col, grid, True)
            neighbors = list(set(neighbors + unvisited))

        return grid
    

class Kruskal():
    """The Kruskal maze-generating algorithm."""

    def __init__(self, h, w):
        assert w >= 3 and h >= 3, "Mazes cannot be smaller than 3x3."
        self.h = h
        self.w = w
        self.H = (2 * self.h) + 1
        self.W = (2 * self.w) + 1
        
    def generate(self):
        """Highest-level method that implements the maze-generating algorithm.

        Returns
        -------
            np.array: returned matrix
        """
        # create empty grid
        grid = np.empty((self.H, self.W), dtype=np.int8)
        grid.fill(1)

        forest = []
        for row in range(1, self.H - 1, 2):
            for col in range(1, self.W - 1, 2):
                forest.append([(row, col)])
                grid[row][col] = 0

        edges = []
        for row in range(2, self.H - 1, 2):
            for col in range(1, self.W - 1, 2):
                edges.append((row, col))
        for row in range(1, self.H - 1, 2):
            for col in range(2, self.W - 1, 2):
                edges.append((row, col))

        shuffle(edges)

        while len(forest) > 1:
            ce_row, ce_col = edges[0]
            edges = edges[1:]

            tree1 = -1
            tree2 = -1

            if ce_row % 2 == 0:  # even-numbered row: vertical wall
                tree1 = sum(
                    [
                        i if (ce_row - 1, ce_col) in j else 0
                        for i, j in enumerate(forest)
                    ]
                )
                tree2 = sum(
                    [
                        i if (ce_row + 1, ce_col) in j else 0
                        for i, j in enumerate(forest)
                    ]
                )
            else:  # odd-numbered row: horizontal wall
                tree1 = sum(
                    [
                        i if (ce_row, ce_col - 1) in j else 0
                        for i, j in enumerate(forest)
                    ]
                )
                tree2 = sum(
                    [
                        i if (ce_row, ce_col + 1) in j else 0
                        for i, j in enumerate(forest)
                    ]
                )

            if tree1 != tree2:
                new_tree = forest[tree1] + forest[tree2]
                temp1 = list(forest[tree1])
                temp2 = list(forest[tree2])
                forest = [
                    x for x in forest if x != temp1
                ]  # faster than forest.remove(temp1)
                forest = [x for x in forest if x != temp2]
                forest.append(new_tree)
                grid[ce_row][ce_col] = 0

        return grid


h, w = 11, 11  # Example maze size (odd numbers work best)
prims = Kruskal(h, w)
maze = prims.generate()

# Display the grid
plt.figure(figsize=(10, 10))
plt.imshow(maze, cmap="gray", interpolation="nearest")

# Remove axes for a cleaner look
plt.xticks([])
plt.yticks([])
plt.grid(False)

# Show the maze
plt.show()