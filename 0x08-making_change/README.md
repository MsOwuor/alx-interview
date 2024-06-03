# Make Change

This project provides a Python function to determine the fewest number of coins needed to meet a given total amount using a dynamic programming approach.

## Function

The main function provided is:

```python
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
