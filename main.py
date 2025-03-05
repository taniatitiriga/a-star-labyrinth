from drawer import draw_maze
from maze import Maze
from a_star import astar_visualized

def main():
    maze_size = 21
    maze = Maze(maze_size)
    grid = maze.generate()
    draw_maze(grid)
    graph = maze.to_graph()

    print("Running A* Pathfinding...")
    astar_visualized(graph, maze.entrance, maze.exit, grid)

if __name__ == "__main__":
    main()
