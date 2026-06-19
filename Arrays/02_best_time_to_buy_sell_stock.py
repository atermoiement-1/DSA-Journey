"""
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode
Difficulty: Easy

Approach:
Maintain the minimum stock price seen so far.
For each day, calculate the profit if sold today.
Update the maximum profit whenever a better profit is found.

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maxProfit = 0
        for price in prices:
            if price < minimum:
                minimum = price
            else:
                maxProfit = max(maxProfit, price - minimum)
        return maxProfit
