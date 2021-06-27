"""
    PROBLEM:
        Given an array of numbers consisting of daily
        stock prices, calculate the maximum amount of
        profit that can be made from buying on one day
        and selling on another.

        In an array of prices, each index represents a
        day, and the value on that index represents the
        price of the stocks on that day.

        Profit = Selling Price - Buying Price
"""

def buy_n_sell_brute_force(prices_array):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    max_profit = 1
    max_profit_index = None

    for i in range(len(prices_array) - 1):
        for j in range(i + 1, len(prices_array)):
            if prices_array[j] - prices_array[i] > max_profit:
                max_profit = prices_array[j] - prices_array[i]
                max_profit_index = i, j

    return {
        'max_profit': max_profit,
        'indexes': max_profit_index
    }