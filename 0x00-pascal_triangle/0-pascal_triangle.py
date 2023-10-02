#!/usr/bin/python3
"""Code to generate the Pascal Triangle for a given integer"""


def pascal_triangle(n):
    """Prints the pascal triangle with the given integer n"""

    result = []
    if n <= 0:
        return result
    
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                result.append(1)
            elif i > 0 and j > 0:
                row.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(row)
    return result