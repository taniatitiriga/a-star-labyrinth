from astar import astar
from maze import Maze
import time


def time_astar(maze_size):
    """Times A* search on 5 random mazes of given size. """
    avg_time = 0
    for _ in range(5):
        # 5 sample random mazes
        maze = Maze(maze_size)
        maze.generate()
        graph = maze.to_graph()
        
        # timer
        start_time = time.time()
        astar(graph, maze.entrance, maze.exit)
        end_time = time.time()
        
        avg_time += (end_time - start_time)
    
    avg_time /= 5
    print(f"Maze size: {maze_size}x{maze_size} | Average time (5 tries): {avg_time:.6f} seconds")
    
    return avg_time
