"""
Problem : Missing Number
Platform : LeetCode
Difficulty : Easy

Approach:
(Mathematical Formula)

Initialize:
Create three variables:

- n : stores the length of the array.
- total : stores the expected sum of numbers from 0 to n using the arithmetic sum formula.
- current : stores the actual sum of all elements present in the array.

Traversal:
Traverse the array once and calculate the sum of all elements.

Observation:
The difference between the expected sum and the actual sum
represents the missing number.

Formula:

Expected Sum = n × (n + 1) / 2

Missing Number = total - current

Time Complexity : O(n)
Space Complexity : O(1)

Pattern Learned:
Mathematical Formula (Arithmetic Sum)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2

        current = 0
        for num in nums:
            current += num

        return total - current
