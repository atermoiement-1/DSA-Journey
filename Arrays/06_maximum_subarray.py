"""
Problem : Maximum Subarray
Platform : LeetCode
Difficulty : Medium

Approach:
Kadane's Algorithm

Initialize:
Create two variables:
- current : stores the current subarray sum.
- maxi : stores the maximum subarray sum found so far.

Traversal:
Iterate through the array once.

For each element:
- Add it to the current subarray sum.
- Update maxi if the current sum becomes larger.
- If the current sum becomes negative, reset it to 0,
  because a negative sum cannot help form a larger subarray
  in the future.

Time Complexity : O(n)
Space Complexity : O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        current = 0
        for num in nums:
            current += num
            if current > maxi:
                maxi = current
            if current < 0:
                current = 0
        return maxi
