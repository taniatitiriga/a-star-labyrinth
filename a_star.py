import matplotlib.pyplot as plt
import time
from heapq import heappush, heappop

def astar(graph, start_node, goal_node):
    open_set = [(0, start_node)]
    came_from = {}
    cost_so_far = {start_node: 0}

    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def rebuild_path(n):
        path = [n]
        while n in came_from:
            n = came_from[n]
            path.append(n)
        return path[::-1]

    while open_set:
        curr_cost, curr_node = heappop(open_set)

        if curr_node == goal_node:
            return rebuild_path(goal_node)

        for neighbor in graph[curr_node]:
            new_cost = cost_so_far[curr_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal_node)
                heappush(open_set, (priority, neighbor))
                came_from[neighbor] = curr_node

    return None

def astar_visualized(graph, start_node, goal_node, maze_grid):
    open_set = [(0, start_node)]
    came_from = {}
    cost_so_far = {start_node: 0}

    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def rebuild_path(n):
        path = [n]
        while n in came_from:
            n = came_from[n]
            path.append(n)
        return path[::-1]

    plt.ion()
    fig, ax = plt.subplots()

    explored = set()

    while open_set:
        curr_cost, curr_node = heappop(open_set)

        if curr_node == goal_node:
            path = rebuild_path(goal_node)
            plot_maze(maze_grid, path, explored, start_node, goal_node, ax)
            plt.ioff()
            plt.show()
            return path

        explored.add(curr_node)

        for neighbor in graph[curr_node]:
            new_cost = cost_so_far[curr_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal_node)
                heappush(open_set, (priority, neighbor))
                came_from[neighbor] = curr_node

        plot_maze(maze_grid, rebuild_path(curr_node), explored, start_node, goal_node, ax)
        time.sleep(0.1)

    plt.ioff()
    plt.show()
    return None

def plot_maze(grid, path, explored, start_node, goal_node, ax):
    ax.clear()
    
    ax.imshow(grid, cmap="gray", interpolation="nearest")

    if explored:
        ex_x, ex_y = zip(*explored)
        ax.scatter(ex_y, ex_x, color='green', label="Explored", s=10)

    if path:
        p_x, p_y = zip(*path)
        ax.scatter(p_y, p_x, color='red', label="Current Path", s=30)

    ax.scatter(start_node[1], start_node[0], color='yellow', label="Start", s=80)
    ax.scatter(goal_node[1], goal_node[0], color='blue', label="Goal", s=80)

    ax.legend(loc="upper right")
    plt.draw()
    plt.pause(0.01)
