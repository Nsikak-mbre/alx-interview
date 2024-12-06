#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.

    Args:
        coins (list): A list of integers representing the coin denominations.
        total (int): The total amount for which we need to find
        the fewest number of coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be met by any combination of coins, return -1.
             If total is 0 or less, return 0.

    Example:
        makeChange([1, 2, 5], 11) -> 3 (5 + 5 + 1)
        makeChange([2], 3) -> -1
    """

    if total <= 0:
        return 0

    # Initialize dp array, where dp[i] is the minimum number of coins needed
    # to make total i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    # Fill the dp array using dynamic programming
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still inf, return -1 as it's not possible to make the
    # total
    return dp[total] if dp[total] != float('inf') else -1
