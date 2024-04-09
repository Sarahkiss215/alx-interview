#!/usr/bin/python3
'''
Returns list showing the Pascal's triangle of n
'''


def pascal_triangle(n):
    '''returns empty list if n <= 0'''
    if n <= 0:
        return []
    triangle = [[1]]
    for m in range(1, n):
        row1 = triangle[-1]
        row2 = [1] * (m + 1)
        for j in range(1, m):
            row2[j] = row1[j-1] + row1[j]
        triangle.append(row2)
    return triangle
