# Maze Visualizer and Solver

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-green?logo=pygame&logoColor=white)
![License](https://img.shields.io/github/license/l-gzn/Maze-Visualizer-Solver)

A dynamic visualization tool that brings graph theory to life. This application demonstrates maze generation and pathfinding algorithms in real-time using a custom-built Pygame interface.

![App Demo](https://via.placeholder.com/800x400.png?text=Main+Hero+GIF+Placeholder)

---

## Key Features

* **Maze Generation:**
    * **Perfect:** Recursive Backtracking ensures exactly one path between any two points.
    * **Non-Perfect:** Introduces cycles and loops for more complex solving scenarios.
* **Pathfinding Suite:** Visualize DFS, BFS, A*, and Dijkstra as they explore the grid.
* **Dynamic Obstacles:** Toggle randomized obstacles that solvers must navigate around.
* **Flexible Layout:** The application automatically adjusts the grid and UI buttons when the window is resized.

---

## Algorithm Demos

| Maze Generation and A* Search (Shortest Path) |
| :---: | :---: |
| ![Generation GIF](assets/a-star.gif)
| *Recursive Backtracking* | *Heuristic-based Navigation* |

---

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/l-gzn/Maze-Visualizer-Solver.git](https://github.com/l-gzn/Maze-Visualizer-Solver.git)
   cd Maze-Visualizer-Solver
   ```

2. **Install dependencies:**
```bash
pip install pygame heapdict

```


3. **Run the application:**
```bash
python main.py

```



---

## Project Structure

The project is organized into a modular structure for better maintainability:

```text
.
├── main.py           # Application entry point
├── src/              # Core logic and classes
│   ├── classes.py    # Grid, Cell, and Button objects
│   └── utils.py      # UI layout and event helpers
├── assets/           # Visual assets
│   └── Buttons/      # UI button icons
└── README.md

```

---

## Technical Overview

### Maze Generation

The generator uses Recursive Backtracking. It treats the grid as a graph where each cell is a node. By removing walls between unvisited neighbors, it creates a tree structure, ensuring no loops and a guaranteed path from start to finish.

### Pathfinding Algorithms

* **A* Search:** Uses a Manhattan distance heuristic to prioritize cells closer to the goal.
* **BFS:** Explores layer by layer to guarantee the shortest path in an unweighted grid.
* **DFS:** Dives deep into branches, creating winding paths characteristic of classic maze solving.
* **Dijkstra:** A weighted search that finds the shortest path, effectively A* without a heuristic in this implementation.

---

## License

Distributed under the MIT License. See LICENSE for more information.

---

**Developed by [l-gzn**](https://www.google.com/search?q=https://github.com/l-gzn)
