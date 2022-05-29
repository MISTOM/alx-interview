#!/usr/bin/python3
"""Rotate 2D matrix module
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]):
    """Rotates a 2D matrix 90 Degrees Clockwise"""
    l = 0
    r = len(matrix) - 1
    while (l < r):
        for i in range(r - l):
            top, bottom = l, r
            # save the topLeft value temporarily
            temp = matrix[top][l + i]
            # move bottomLeft into topLeft
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottomRight into bottomLeft
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move topRight into bottomRight
            matrix[bottom][r - i] = matrix[top + i][r]

            # move topLeft to topRight
            matrix[top + i][r] = temp
        r -= 1
        l += 1
