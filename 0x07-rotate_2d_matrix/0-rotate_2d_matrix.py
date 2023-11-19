#!/usr/bin/python3
"""Code to rotate a 2d
Matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """rotates the matrix"""
    start = 0
    end = len(matrix) - 1

    while start < end:
        """main logic"""
        for i in range(end - start):
            top = start
            bottom = end

            top_start = matrix[top][start + i]
            matrix[top][start + i] = matrix[bottom - i][start]
            matrix[bottom - i][start] = matrix[bottom][end - i]
            matrix[bottom][end - i] = matrix[top + i][end]
            matrix[top + i][end] = top_start

        end -= 1
        start += 1
