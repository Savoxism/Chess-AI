import os

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Board dimension
COLS = 8
ROWS = 8
SQSIZE = WIDTH // COLS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOUNDS_DIR = os.path.join(BASE_DIR, "assets", "sounds")
