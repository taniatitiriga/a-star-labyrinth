from maze import Maze, draw_maze
from timer import time_astar
from astar_visualizer import astar_visualized

def main():
    option = input("Option:\n1. Visualize A*\n2. Test A*\n")
    if option == "1":
        maze_size = int(input("Maze size:"))
        if maze_size not in range(4, 100):
            print("Choose another size.")
        else:
            maze = Maze(maze_size)
            grid = maze.generate()
            graph = maze.to_graph()
            astar_visualized(graph, maze.entrance, maze.exit, grid)
    elif option == "2":
        sizes = [10, 100, 1000]
        for size in sizes:
            time_astar(size)

    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
