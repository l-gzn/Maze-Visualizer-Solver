# Maze Visualizer & Solver

A Pygame-based application for **generating, visualizing, and solving mazes** using various classical pathfinding algorithms, with optional obstacles and dynamic resizing support.

---

## Features

- **Maze Generation**
  - *Perfect Maze:* Generated using recursive backtracking with no loops.
  - *Non-perfect Maze:* Includes optional loops for more complex topologies.
  - *Obstacle Placement:* Randomized and visualized as black squares.

- **Algorithms**
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - A* Search
  - Dijkstra's Algorithm (A* with zero heuristic)

- **Interactive UI**
  - Clickable buttons for:
    - Generating maze types
    - Adding/removing obstacles
    - Choosing endpoints (bottom-right or deepest)
    - Running solving algorithms

- **Visualization**
  - Real-time drawing of maze construction and pathfinding steps.
  - Custom color-coding:
    - Purple: Visited path
    - Red: Final path
    - Black: Obstacles
    - Orange: Current exploration
    - Green: Endpoint

- **Responsive Layout**
  - Automatically adjusts button layout and cell size when window is resized.

---

## Project Structure
```text
├── main.py         # Entry point with Pygame loop and UI logic
├── config.py       # Global constants and configuration
├── maze.py         # Core `Grid` and `Cell` classes
├── ui.py           # UI classes like `Button`
├── utils.py        # Utility functions (quit handling, layout updates)
├── classes.py      # (Now empty, can be deleted)
├── Buttons/        # Folder with button images
├── README.md       # You're reading it!
```

---

## 🧠 How It Works

### Grid Representation
- The maze is a grid of `Cell` objects, each with walls on four sides.
- Recursive backtracking removes walls to form paths.

---

## 🕹️ Controls

| Action                        | Description                              |
|------------------------------|------------------------------------------|
| `Perfect`                    | Generate a perfect maze                  |
| `Non-perfect`                | Generate maze with loops                 |
| `Obstacles / No Obstacles`  | Toggle obstacle placement                |
| `Deepest`                    | Set the end cell as the farthest from start |
| `Bottom Right`              | Set the end cell as the bottom-right corner |
| `DFS`, `BFS`, `A*`, `Dijkstra` | Solve the maze using the chosen algorithm |

---

## Requirements

- Python 3.7+
- [Pygame](https://www.pygame.org/)
- [heapdict](https://pypi.org/project/heapdict/)

### Install dependencies

```bash
pip install pygame heapdict
