#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """
    returns the fewest number of operations needed
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            n = n / b
            a += b
        b += 1
    return a