#!/usr/bin/python3
"""
Module for determining the winner of a prime game.
"""


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the rounds.

    Returns:
        str: "Maria" if she wins more rounds, "Ben" if he wins more rounds,
             or None if there is no clear winner.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number to consider primes up to
    max_n = max(nums)

    # Sieve of Eratosthenes to precompute prime numbers
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute cumulative prime counts
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 1:  # Maria wins if prime count is odd
            maria_wins += 1
        else:  # Ben wins if prime count is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
