from heapq import heappush, heappop

def astar(graph, start_node, goal_node):
    """Runs A* algorithm for timing."""
    
    open_set = [(0, start_node)]
    came_from = {}
    cost_so_far = {start_node: 0}

    def heuristic(node, goal):
        """Manhattan distance for 2D graph = vertical + horizontal distance"""
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def rebuild_path(n):
        # add all previous nodes to reconstruct path
        path = [n]
        while n in came_from:
            n = came_from[n]
            path.append(n)
        return path[::-1]

    while open_set:
        # pop the lowest weight node
        _, curr_node = heappop(open_set)

        if curr_node == goal_node:
            # check if finished
            return rebuild_path(goal_node)

        for neighbor in graph[curr_node]:
            new_cost = cost_so_far[curr_node] + 1
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                # update neighbours
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal_node)
                
                # add neighbours with weights to heap
                heappush(open_set, (priority, neighbor))
                came_from[neighbor] = curr_node

    return None
