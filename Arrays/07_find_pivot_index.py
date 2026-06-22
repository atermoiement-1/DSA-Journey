"""
Problem : Find Pivot Index
Platform : LeetCode
Difficulty : Easy

Approach:
Prefix Sum / Running Sum

Initialize:
Create two variables:

- total : stores the sum of all elements in the array.
- left : stores the running sum of elements to the left of the current index.

Traversal:
Iterate through the array once.

For each element:

- Calculate the right-side sum using:

      right_sum = total - left - nums[i]

- If left equals right_sum, the current index is the pivot index.
- Otherwise, add the current element to left and continue.
- If no pivot index is found, return -1.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
