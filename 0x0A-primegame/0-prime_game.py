#!/usr/bin/python3
def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None

    # Step 1: Find the maximum n to limit our prime number calculations
    max_n = max(nums)

    # Step 2: Generate primes up to max_n using Sieve of Eratosthenes
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Step 3: Precompute prime counts
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 4: Simulate the game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If prime_count[n] is odd, Maria wins (she plays first)
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 5: Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
