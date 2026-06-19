# ============================================
# Problem: Two Sum
# LeetCode #1 | Difficulty: Easy
# Topic: Arrays, HashMap
# ============================================
#
# Problem Statement:
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.
#
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9
#
# ============================================
# Approach: HashMap (One Pass)
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in dict:
                return [dict[compliment], i]
            dict[nums[i]] = i
        return []

# ============================================
# What I learned:
# - Using a HashMap reduces time from O(n²) to O(n)
# - Store what you've SEEN so far, check what you NEED
# ============================================
