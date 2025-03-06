import time
from maze import Maze
from astar import astar

def time_astar(maze_size):
    """Times A* search on 5 random mazes of given size. """
    avg_time = 0
    for i in range(5):
        maze = Maze(maze_size)
        maze.generate()
        graph = maze.to_graph()
        
        start, goal = maze.entrance, maze.exit
        
        start_time = time.time()
        path = astar(graph, start, goal)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        avg_time += elapsed_time
    
    avg_time /= 5
    print(f"Maze size: {maze_size}x{maze_size} | Average time (5 tries): {avg_time:.6f} seconds")
    
    return elapsed_time
