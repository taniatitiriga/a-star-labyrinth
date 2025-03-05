from drawer import draw_maze
# from maze_generator import generate_maze
from maze import Maze

maze = Maze(7)
maze = maze.generate()
draw_maze(maze)