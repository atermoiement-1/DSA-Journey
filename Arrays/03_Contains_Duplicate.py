"""
Problem: Contains Duplicate
Platform: LeetCode
Difficulty: Easy

Approach:
Sort the array first.
If any two adjacent elements are equal,
a duplicate exists.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
