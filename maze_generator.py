import random

class maze_grid:
    WALL = 0
    PASSAGE = 1

def generate_maze(size: int) -> list[list[int]]:
    def get_neighbors(r, c):
        neighbours = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            x, y = r + dx, c + dy
            if 0 <= x < size and 0 <= y < size and maze_map[x][y] != maze_grid.PASSAGE:
                neighbours.append((x, y))
        return neighbours

    size = size * 2 + 1
    maze_map = [[maze_grid.WALL] * size for _ in range(size)]

    stack = [(1, 1)]
    maze_map[1][1] = maze_grid.PASSAGE

    while stack:
        i, j = stack[-1]
        maze_map[i][j] = maze_grid.PASSAGE

        neighbors = get_neighbors(i, j)

        if neighbors:
            neighbor = random.choice(neighbors)

            maze_map[(i + neighbor[0]) // 2][(j + neighbor[1]) // 2] = maze_grid.PASSAGE

            stack.append(neighbor)
        else:
            stack.pop()

    # Create the entrance and the exit
    maze_map[0][1] = maze_grid.PASSAGE
    maze_map[size - 1][size - 2] = maze_grid.PASSAGE

    return maze_map