#!/usr/bin/python3
"""returns perimeter of island"""


def island_perimeter(grid):
    """returns perimter of island in grid"""
    perimeter = 0
    if type(grid) != list:
        return 0

    length = len(grid)

    for i, row in enumerate(grid):
        row_length = len(row)
        for j, box in enumerate(row):
            if box == 0:
                continue
            corner = (
                    i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                    j == row_length - 1 or (row_length > j + 1
                                            and row[j + 1] == 0),
                    i == length - 1 or (len(grid[i + 1]) > j
                                        and grid[i + 1][j] == 0),
                    j == 0 or row[j - 1] == 0,
                    )
            perimeter += sum(corner)

    return perimeter
