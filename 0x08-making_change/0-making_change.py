#!/usr/bin/python3
"""Making Change Algorithm
"""


def makeChange(coins, total) -> int:
    """Determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0

    remainder = total
    no_of_coins = 0
    index = 0
    sorted_coins = sorted(coins, reverse=True)
    length = len(coins)

    while remainder > 0:
        if index >= length:
            return -1

        if remainder - sorted_coins[index] >= 0:
            remainder -= sorted_coins[index]
            no_of_coins += 1
        else:
            index += 1

    return no_of_coins
