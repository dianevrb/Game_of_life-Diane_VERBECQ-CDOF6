import os
import time
import numpy as np

def print_grid(grid):
    """
    Displays the grid in the terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(['#' if cell else '.' for cell in row]))
    print()

def update_grid(grid):
    """
    Updates the grid based on the rules of the Game of Life.
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live_neighbors(grid, r, c)
            if grid[r][c] == 1:
                # A live cell survives with 2 or 3 live neighbors
                new_grid[r][c] = 1 if live_neighbors in (2, 3) else 0
            else:
                # A dead cell becomes alive with exactly 3 live neighbors
                new_grid[r][c] = 1 if live_neighbors == 3 else 0
    return new_grid

def count_live_neighbors(grid, row, col):
    """
    Counts the number of live neighbors around a cell.
    """
    rows, cols = len(grid), len(grid[0])
    live_neighbors = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                live_neighbors += grid[nr][nc]
    return live_neighbors

def main():
    # Grid dimensions
    rows, cols = 20, 20

    # Random initialization of the grid
    grid = np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])

    print("Welcome to the Game of Life!")
    print("Simulation with a 20x20 grid and random initialization.")
    print("Press Ctrl+C to exit.\n")

    try:
        while True:
            print_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nSimulation stopped by the user. Thanks for playing!")

if __name__ == "__main__":
    main()
