#!/usr/bin/python3
"""
determine the fewest
number of coins needed
to meet a given amount
"""


def makeChange(coins, total):
    """determine the fewest number of
        coins needed to meet a given
        amount
    """
    if total <= 0:
        return 0

    copy = total
    total_coins = 0
    idx = 0
    sorted_coins = sorted(coins, reverse=True)
    num = len(coins)

    while copy > 0:
        if idx >= num:
            return -1
        if copy - sorted_coins[idx] >= 0:
            copy -= sorted_coins[idx]
            total_coins += 1
        else:
            idx += 1

    return total_coins
