#!/usr/bin/python3
"""Algorithm to Solve Island Perimeter Problem
"""


def island_perimeter(grid) -> int:
    """
    Calculates the perimeter of the island described in grid
    """

    grid_len = len(grid)
    perimeter = 0

    for i in range(grid_len):
        for j in range(len(grid[i])):

            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    perimeter += 1

                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    perimeter += 1

                if (j <= 0 or grid[i][j - 1] == 0):
                    perimeter += 1

                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    perimeter += 1

    return perimeter
