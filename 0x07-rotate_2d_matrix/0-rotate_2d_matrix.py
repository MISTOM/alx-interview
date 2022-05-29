#!/usr/bin/python3
"""Rotate 2D matrix module
"""
# from typing import List


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 Degrees Clockwise"""
    left = 0
    r = len(matrix) - 1
    while (left < r):
        for i in range(r - left):
            top, bottom = left, r
            # save the topLeft value temporarily
            temp = matrix[top][left + i]
            # move bottomLeft into topLeft
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottomRight into bottomLeft
            matrix[bottom - i][left] = matrix[bottom][r - i]

            # move topRight into bottomRight
            matrix[bottom][r - i] = matrix[top + i][r]

            # move topLeft to topRight
            matrix[top + i][r] = temp
        r -= 1
        left += 1
