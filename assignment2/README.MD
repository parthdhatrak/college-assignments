A* Search Algorithm

Aim

To implement the A Search Algorithm* in Python to find the optimal path between a start node and a goal node using:

g(n) = actual cost from the start node

h(n) = heuristic estimated cost to the goal

f(n) = total estimated cost

The main formula used is:

f(n) = g(n) + h(n)

Python Code

import heapq


def a_star(graph, heuristic, start, goal):
    # Priority queue containing (f_cost, node)
    open_list = [(0, start)]

    # Actual cost from start node to every node
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    # Stores parent of each node for path reconstruction
    parent = {node: None for node in graph}

    while open_list:
        # Select the node with the smallest f(n)
        current_f, current = heapq.heappop(open_list)

        # If goal is reached, reconstruct the path
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        # Explore all neighboring nodes
        for neighbor, cost in graph[current]:

            # Calculate new actual cost g(n)
            new_g_cost = g_cost[current] + cost

            # Check if a better path is found
            if new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                parent[neighbor] = current

                # Calculate f(n) = g(n) + h(n)
                f_cost = new_g_cost + heuristic[neighbor]

                # Add neighbor to priority queue
                heapq.heappush(open_list, (f_cost, neighbor))

    # Return if no path exists
    return None, float('inf')


# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
}


# Heuristic values h(n)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}


# Starting and goal nodes
start = 'A'
goal = 'E'


# Execute A* algorithm
path, cost = a_star(graph, heuristic, start, goal)


# Display result
if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")

Output

Optimal Path: A -> B -> C -> D -> E
Total Cost: 7

Working Principle

A* selects the node with the smallest value of:

f(n) = g(n) + h(n)

Where:

g(n) is the actual cost travelled from the starting node to the current node.

h(n) is the estimated cost from the current node to the goal.

f(n) is the estimated total cost of the path through that node.

For example, if:

g(C) = 3
h(C) = 2

Then:

f(C) = 3 + 2 = 5

The algorithm continues selecting the node with the smallest f(n) until it reaches the goal node.

Result

The optimal path found from A to E is:

A -> B -> C -> D -> E

The total path cost is:

7
