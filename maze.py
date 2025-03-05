import random

class Maze:
    """
    A class to represent a randomly generated maze.
    Attributes:
    -----------
    WALL : int
    PASSAGE : int
        Constants representing walls and passages in the maze.
    size : int
        The size of the maze (modified to be odd).
    grid : list[list[int]]
        A 2D list representing the maze structure (walls and passages). Used for plotting.
    entrance : tuple[int, int]
        Coordinates of the entrance of the maze.
    exit : tuple[int, int]
        Coordinates of the exit of the maze.
    """
    # maze as a matrix of 0 and 1 for plotting
    WALL = 0
    PASSAGE = 1

    def __init__(self, size: int):
        # initialize an odd-sized maze
        self.size = size if size % 2 else size + 1
        
        # initialize maze full (all walls)
        self.grid = [[self.WALL] * self.size for _ in range(self.size)]
        
        # define entrance and exit
        self.entrance = (0, 1)
        self.exit = (self.size - 1, self.size - 2)

    def _get_neighbors(self, r, c):
        """ Returns valid neighbors of the current cell. """
        neighbors = []
        
        # check neighbours (at a distance of 2)
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            x, y = r + dx, c + dy
            if 0 <= x < self.size and 0 <= y < self.size and self.grid[x][y] != self.PASSAGE:
                neighbors.append((x, y))
        
        return neighbors

    def generate(self):
        """ Generates a random maze using DFS. """
        
        # stack > recursiveness
        stack = [(1, 1)]
        # start below the entrance
        self.grid[1][1] = self.PASSAGE

        while stack:
            i, j = stack[-1]
            self.grid[i][j] = self.PASSAGE
            
            # clear 2 cells at a time to ensure the existence of walls between parallel corridors
            neighbors = self._get_neighbors(i, j)
            if neighbors:
                # choose a random neighbour to move towards
                neighbor = random.choice(neighbors)

                # clear cell between current and neighbour
                self.grid[(i + neighbor[0]) // 2][(j + neighbor[1]) // 2] = self.PASSAGE
                # clear neighbour next and continue
                stack.append(neighbor)
            else:
                stack.pop()

        # clear entrance and exit
        self.grid[self.entrance[0]][self.entrance[1]] = self.PASSAGE
        self.grid[self.exit[0]][self.exit[1]] = self.PASSAGE
        
        return self.grid
    
    def to_graph(self):
        """Converts the maze into an adjacency list graph."""
        graph = {}
        rows, cols = len(self.grid), len(self.grid[0])

        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == self.PASSAGE:
                    neighbors = []
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and self.grid[nr][nc] == self.PASSAGE:
                            neighbors.append((nr, nc))
                    graph[(r, c)] = neighbors

        return graph

