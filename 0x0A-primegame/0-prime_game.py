#!/usr/bin/python3
"""script for prime game"""


def isWinner(x, nums):
    """gets winner of prime game"""
    if x < 1 or not nums:
        return None
    first_wins, second_wins = 0, 0
    plc = max(nums)
    prime_nums = [True for _ in range(1, plc + 1, 1)]
    prime_nums[0] = False

    for i, prime_number in enumerate(prime_nums, 1):
        if i == 1 or not prime_number:
            continue
        for j in range(i + i, plc + 1, i):
            prime_nums[j - 1] = False

    for _, plc in zip(range(x), nums):
        no_primes = len(list(filter(lambda x: x, prime_nums[0:plc])))
        second_wins += no_primes % 2 == 0
        first_wins += no_primes % 2 == 1

    if first_wins == second_wins:
        return None
    return "Maria" if first_wins > second_wins else "Ben"
