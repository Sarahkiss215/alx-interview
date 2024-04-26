#!/usr/bin/python3
"""
Module for minimum operations
"""


def minOperations(n):
    """Gets fewest number of operations needed
    """
    i = 0
    j = 2
    while n > 1:
        while n % j == 0:
            i += j
            n /= j
        j += 1
    return i
