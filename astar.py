from heapq import heappush, heappop

def astar(graph, start_node, goal_node):
    """Runs A* algorithm for timing."""
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
        _, curr_node = heappop(open_set)

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
