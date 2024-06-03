#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins needed
to meet a given total amount using a dynamic programming approach.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: Fewest number of coins needed to meet the total amount.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0
    
    # Initialize dp array with a large number (total + 1) which is considered infinity here
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # No coins needed to make total 0

    # Loop through each coin
    for coin in coins:
        # Update dp for all amounts from coin to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still total + 1, it means we couldn't make up the total with the given coins
    return dp[total] if dp[total] != total + 1 else -1

