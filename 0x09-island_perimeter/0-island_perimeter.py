#!/usr/bin/python3
"""
Module for island perimeter.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.

    Args:
        grid (List[List[int]]): A list of lists representing the insland.

    Returns:
        ValueError: If the grid is not rectangular.
    """
    if not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Grid is not rectangular")

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
