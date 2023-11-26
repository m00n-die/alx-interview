#!/usr/bin/python3
"""Code to determine the fewest
number of coins needed to meet
a given amount 'total'
"""

import sys


def makeChange(coins, total):
    """the main function"""
    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1
    totalChange = 0
    coins = sorted(coins)[::-1]

    for val in coins:
        while val <= total:
            total -= val
            totalChange += 1

    if total == 0:
        return totalChange

    return -1
