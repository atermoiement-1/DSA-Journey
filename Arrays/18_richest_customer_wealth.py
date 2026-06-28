"""
Problem : Richest Customer Wealth
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Nested Traversal

Observation:
Each row in the 2D array represents a customer, and each column
represents the money available in one of their bank accounts.

The wealth of a customer is the sum of all values in their row.

Initialize:
Create:
- maxi : Stores the maximum wealth found so far.

Traversal:
Traverse each row of the 2D array.

For every customer:
- Create a variable 'wealth' to calculate the total wealth.
- Traverse all bank accounts of the current customer.
- Add each account balance to the wealth.
- Compare the current wealth with the maximum wealth found so far.
- Update the maximum value if required.

Finally, return the maximum wealth.

Time Complexity : O(m × n)
Space Complexity : O(1)

Pattern Learned:
Matrix Traversal
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in range(len(accounts)):
            count = 0
            for j in range(len(accounts[i])):
                count += accounts[i][j]
            maxi = max(maxi, count)
        return maxi
