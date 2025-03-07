from astar_visualizer import astar_visualized
from timer import time_astar
from maze import Maze

def main():
    option = input("Option:\n1. Visualize A*\n2. Test A*\n")
    if option == "1":
        # Maze visualizer with input size
        maze_size = int(input("Maze size:"))
        if maze_size not in range(4, 100):
            print("Choose another size.")
        else:
            maze = Maze(maze_size)
            grid = maze.generate()
            graph = maze.to_graph()
            astar_visualized(graph, maze.entrance, maze.exit, grid)
    elif option == "2":
        # Speed test randomly generated mazes (no visualization)
        sizes = [10, 100, 1000]
        for size in sizes:
            time_astar(size)

    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
