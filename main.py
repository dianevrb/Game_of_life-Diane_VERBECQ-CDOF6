import os
import time
import numpy as np

def print_grid(grid):
    """
    Affiche la grille dans le terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(['#' if cell else '.' for cell in row]))
    print()


def update_grid(grid):
    """
    Met à jour la grille selon les règles du Game of Life.
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live_neighbors(grid, r, c)
            if grid[r][c] == 1:
                # Une cellule vivante survit avec 2 ou 3 voisins vivants
                new_grid[r][c] = 1 if live_neighbors in (2, 3) else 0
            else:
                # Une cellule morte devient vivante avec exactement 3 voisins vivants
                new_grid[r][c] = 1 if live_neighbors == 3 else 0
    return new_grid


def count_live_neighbors(grid, row, col):
    """
    Compte le nombre de voisins vivants autour d'une cellule.
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
    # Dimensions de la grille
    rows, cols = 20, 20

    # Initialisation aléatoire de la grille
    grid = np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])

    print("Bienvenue dans le Game of Life!")
    print("Simulation avec une grille de 20x20 et une initialisation aléatoire.")
    print("Appuyez sur Ctrl+C pour quitter.\n")

    try:
        while True:
            print_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nSimulation arrêtée par l'utilisateur. Merci d'avoir joué!")


if __name__ == "__main__":
    main()
