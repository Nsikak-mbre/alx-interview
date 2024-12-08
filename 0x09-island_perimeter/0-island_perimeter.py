#!/usr/bin/python3
"""Module for island_perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    :param grid: List[List[int]] - a rectangular grid representing
    land and water
    :return: int - the perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Add 4 sides of the cell initially
                perimeter += 4

                # Check for adjacent land cells and subtract shared sides
                if r > 0 and grid[r - 1][c] == 1:  # Top
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Left
                    perimeter -= 2

    return perimeter
