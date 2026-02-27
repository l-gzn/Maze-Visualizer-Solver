import os
import random
import sys
import pygame


# Add project root to the Python path to find the new package
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from maze_visualizer import config
from maze_visualizer.maze import Grid
from maze_visualizer.ui import Button
from maze_visualizer.utils import handle_quit, update_layout

pygame.init()

# --- Window Setup ---
HEIGHT = config.HEIGHT
WIDTH = config.WIDTH
SCALE_FACTOR = HEIGHT / config.BASE_HEIGHT
UI_WIDTH_SCALED = 200
CELL_SIZE = config.calculate_cell_size(HEIGHT, config.COLS)
WIN = pygame.display.set_mode((WIDTH + 2, HEIGHT + 2), pygame.RESIZABLE)
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

# --- Game State Variables ---
grid = Grid(config.ROWS, config.COLS, CELL_SIZE, WIN)
Maze_done = False
Solved = False
deepest = None
obs = False

# --- Load Button Images ---
perfect_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "Perfect.png")).convert_alpha()
non_perfect_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "Non_perfect.png")).convert_alpha()
deepest_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "Deepest.png")).convert_alpha()
bottom_right_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "Bottom_right.png")).convert_alpha()
obstacles_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "Obstacles.png")).convert_alpha()
no_obstacles_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "No_obstacles.png")).convert_alpha()
dfs_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "DFS.png")).convert_alpha()
bfs_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "BFS.png")).convert_alpha()
astar_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "Astar.png")).convert_alpha()
dijkstra_img = pygame.image.load(os.path.join(config.BUTTONS_DIR, "Dijkstra.png")).convert_alpha()

def create_buttons(button_x, scale):
    return {
        "perfect": Button(button_x, int(0 * 50 * scale), perfect_img, scale=0.95 * scale),
        "non_perfect": Button(button_x, int(1 * 50 * scale), non_perfect_img, scale=0.95 * scale),
        "deepest": Button(button_x, int(2 * 50 * scale), deepest_img, scale=0.95 * scale),
        "bottom_right": Button( button_x, int(3 * 50 * scale), bottom_right_img, scale=0.95 * scale),
        "obstacles": Button(button_x, int(4 * 50 * scale), obstacles_img, scale=0.95 * scale),
        "no_obstacles": Button(button_x, int(5 * 50 * scale), no_obstacles_img, scale=0.95 * scale),
        "dfs": Button(button_x, int(6 * 50 * scale), dfs_img, scale=0.95 * scale),
        "bfs": Button(button_x, int(7 * 50 * scale), bfs_img, scale=0.95 * scale),
        "astar": Button(button_x, int(8 * 50 * scale), astar_img, scale=0.95 * scale),
        "dijkstra": Button(button_x, int(9 * 50 * scale), dijkstra_img, scale=0.95 * scale),
        }


def handle_maze_generation(loops, obstacles):
    """Handles the logic for generating a new maze."""
    global grid, Maze_done, Solved, deepest

    Maze_done = False
    WIN.fill("black", ((0, 0), (WIDTH - UI_WIDTH_SCALED, HEIGHT)))
    pygame.display.update()

    random_seed = random.randint(0, 1000)
    print(f"Seed:{random_seed}")
    grid = Grid(config.ROWS, config.COLS, CELL_SIZE, WIN, seed=random_seed)

    # Maze generation loop
    loop_counter = 0
    while grid.current_cell:
        handle_quit()
        grid.maze_gen(loops=loops, obstacles=obstacles)
        loop_counter += 1
        if loop_counter % 100 == 0:
            pygame.display.update()

    pygame.display.update()

    grid.adjacency_list = grid.get_adjacency_list()

    # Find and color the deepest cell
    deepest = grid.bfs(find_deepest=True)
    deep_row, deep_col = grid.num_to_ij(deepest)
    grid.draw_square(deep_row, deep_col, background_col="green")

    Maze_done = True
    Solved = False

def handle_solve_request(algorithm, **kwargs):
    """Handles the logic for solving the maze with a given algorithm."""
    global Solved
    if not Maze_done:
        return

    if Solved:
        grid.new_solve(deepest, obs)

    path = algorithm(end_cell=grid.end, **kwargs)

    if path:
        print(f"Length: {len(path)}")
        if obs:
            grid.redraw_obstacles(path)
            grid.count_obstacles(path)

    Solved = True

BUTTON_X = config.BUTTON_X
buttons = create_buttons(BUTTON_X, SCALE_FACTOR)

# --- Main Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            CELL_SIZE, BUTTON_X, SCALE_FACTOR = update_layout(HEIGHT, WIDTH, config.COLS)
            UI_WIDTH_SCALED = int(200 * SCALE_FACTOR)
            buttons = create_buttons(BUTTON_X, SCALE_FACTOR)

    if buttons["obstacles"].draw(WIN):
        obs = True

    if buttons["no_obstacles"].draw(WIN):
        obs = False
    
    if obs:
        WIN.fill(
            "black",
            rect=(
                (BUTTON_X, int(200 * SCALE_FACTOR)), 
                (UI_WIDTH_SCALED, int(50 * SCALE_FACTOR))
                )
        )

    if not obs:
        WIN.fill(
            "black",
            rect=(
                (BUTTON_X, int(250 * SCALE_FACTOR)), 
                (UI_WIDTH_SCALED, int(50 * SCALE_FACTOR))
                )
        )

    if buttons["perfect"].draw(WIN):
        handle_maze_generation(loops=False, obstacles=obs)

    if buttons["non_perfect"].draw(WIN):
        handle_maze_generation(loops=True, obstacles=obs)

    if buttons["deepest"].draw(WIN):
        grid.end = deepest

    if buttons["bottom_right"].draw(WIN):
        grid.end = config.ROWS * config.COLS

    if grid.end == config.ROWS * config.COLS:
        WIN.fill(
            "black",
            rect=(
                (BUTTON_X, int(150 * SCALE_FACTOR)), 
                (UI_WIDTH_SCALED, int(50 * SCALE_FACTOR))
            )
        )

    if grid.end == deepest and grid.end != config.ROWS * config.COLS:
        WIN.fill(
            "black",
            rect=(
                (BUTTON_X, int(100 * SCALE_FACTOR)), 
                (UI_WIDTH_SCALED, int(50 * SCALE_FACTOR))
                )
        )

    if buttons["dfs"].draw(WIN):
        handle_solve_request(grid.dfs)

    if buttons["bfs"].draw(WIN):
        handle_solve_request(grid.bfs)

    if buttons["astar"].draw(WIN):
        handle_solve_request(grid.a_star, h_mult=config.H_MULT)

    if buttons["dijkstra"].draw(WIN):
        handle_solve_request(grid.a_star, dijkstra=True)

    clock.tick(120)
    pygame.display.update()

pygame.quit()
