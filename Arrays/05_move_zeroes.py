"""
Problem: Move Zeroes
Platform: LeetCode
Difficulty: Easy

Approach:
Use a two-pointer technique.

First Pass:
Maintain a pointer called 'size' that represents the position
where the next non-zero element should be placed.

Traverse the array and whenever a non-zero element is found,
place it at index 'size' and increment 'size'.

Second Pass:
After all non-zero elements have been moved to the front,
fill the remaining positions in the array with zeroes.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        size = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[size] = nums[i]
                size += 1
        while size < len(nums):
            nums[size] = 0
            size += 1

