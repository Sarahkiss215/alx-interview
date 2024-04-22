#!/usr/bin/python3


def minOperations(n):
    """Gets fewest number of operations needed
    """
    i = 0
    j = 2
    while n > 1:
        while n % j == 0:
            i += j
            i /= j
        i += 1
    return j
