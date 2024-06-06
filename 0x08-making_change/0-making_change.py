#!/usr/bin/python3

"""
Determines the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    balance = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            balance += 1
        if (total == 0):
            return balance
    return -1
