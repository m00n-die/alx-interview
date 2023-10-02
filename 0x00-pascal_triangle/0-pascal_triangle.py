#!/usr/bin/python3
"""Code to generate the Pascal Triangle for a given integer"""


def pascal_triangle(n):
    """Prints the pascal triangle with the given integer n"""

    result = []
    if n <= 0:
        return result
    
    for i in range(1, n + 1):
        row = []
        first = 1
        
        for j in range(1, i + 1):
            row.append(first)
            first = first * (i - j) // j
        result.append(row)
   
    return result