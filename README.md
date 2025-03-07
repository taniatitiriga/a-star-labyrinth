# a-star-labyrinth
## Project overview
Program to generate random mazes and solve them using the A* search algorithm. Includes:
- `matplotlib` animation for understanding the algorithm
- benchmarking on random mazes

## Requirements
Ensure you have Python 3.7+ installed.
```py
python --version
```
Dependencies:
- `matplotlib` for visualization:
```py
pip install matplotlib
```
- `heapq` for A* algorithm:
```py
pip install heapq
```
- `time` for benchmarking:
```
pip install time
```
- `random` for maze generation:
```py
pip install random
```
## Launch
```py
python main.py
```
## Run
Choose an option out of the following:
1. Visualize A* - runs the animation of a random maze being solved by A*
2. Test A* - benchmarks 5 random mazes for the sizes: 10x10, 100x100, 1000x1000
