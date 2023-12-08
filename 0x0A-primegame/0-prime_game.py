#!/usr/bin/python3
"""Prime Game
"""


def isPrime(n):
    """checks if a number is prime"""
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True


def calculatePrime(n, prime):
    """calculate the primes"""

    top = prime[-1]
    if n > top:
        for i in range(top + 1, n + 1):
            if isPrime(i):
                prime.append(i)
            else:
                prime.append(0)


def isWinner(x, nums):
    """the actual function"""

    wins = {"Maria": 0, "Ben": 0}
    prime = [0, 0, 2]
    calculatePrime(max(nums), prime)

    for val in range(x):
        sum_options = sum((i != 0 and i <= nums[val])
                          for i in prime[:nums[val] + 1])

        if (sum_options % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    else:
        return "Ben"

    return None
