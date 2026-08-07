# BFS Visualizer (Python)

A simple **Breadth-First Search (BFS) Visualizer** built using Python. This project allows users to create a graph, add vertices and edges, and visualize the BFS traversal through a graphical user interface (GUI).

## Features

* Add vertices dynamically.
* Add edges between vertices.
* Display the graph as an adjacency list.
* Perform Breadth-First Search (BFS) from any starting vertex.
* Display the BFS traversal order.
* Simple and easy-to-use GUI.

---

## Technologies Used

* Python 3.x
* Tkinter (GUI)
* Collections (`deque`) for BFS

> **Optional:** If using the graph drawing version:
>
> * NetworkX
> * Matplotlib

---

## Project Structure

```
BFS-Visualizer/
│── bfs.py          # Main Python program
│── README.md       # Project documentation
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/bfs-visualizer.git
```

2. Navigate to the project folder:

```bash
cd bfs-visualizer
```

3. Run the program:

```bash
python bfs.py
```

---

## Sample Graph

Vertices:

```
1
2
3
4
```

Edges:

```
1 - 2
1 - 3
2 - 4
```

Starting Vertex:

```
1
```

---

## Sample Output

```
BFS Traversal:
1 → 2 → 3 → 4
```

---

## BFS Algorithm

1. Start from the given source vertex.
2. Mark the source as visited.
3. Insert it into a queue.
4. Remove a vertex from the queue.
5. Visit all unvisited adjacent vertices.
6. Repeat until the queue becomes empty.

---

## Time Complexity

| Operation     | Complexity   |
| ------------- | ------------ |
| BFS Traversal | **O(V + E)** |

Where:

* **V** = Number of Vertices
* **E** = Number of Edges

---

## Space Complexity

**O(V)**

---

## Future Improvements

* DFS Visualization
* Dijkstra's Algorithm
* Animated BFS traversal
* Directed graph support
* Weighted graph visualization
* Save and load graphs

---

## Author

**Parth D**

---

## License

This project is available for learning and educational purposes.
