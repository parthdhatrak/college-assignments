from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("\nBFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# User Input
graph = {}

n = int(input("Enter the number of vertices: "))

print("\nEnter each vertex and its adjacent vertices.")

for i in range(n):
    vertex = input(f"\nEnter vertex {i+1}: ")
    neighbors = input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
    graph[vertex] = neighbors

start = input("\nEnter the starting vertex for BFS: ")

bfs(graph, start)