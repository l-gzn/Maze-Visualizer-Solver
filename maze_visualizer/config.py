import os

# --- Dirs ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUTTONS_DIR = os.path.join(BASE_DIR, "Buttons")

# --- Screen ---
HEIGHT = 600
WIDTH = HEIGHT + 200

# --- Maze ---
ROWS, COLS = 200, 200
H_MULT = 1.0

# --- UI ---
UI_WIDTH = 200 
BUTTON_X = WIDTH - UI_WIDTH + 5
BASE_HEIGHT = 600 

def calculate_cell_size(height, cols):
    return height // cols
