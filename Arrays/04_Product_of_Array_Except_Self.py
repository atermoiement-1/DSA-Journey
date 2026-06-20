"""
Problem: Product of Array Except Self
Platform: LeetCode
Difficulty: Medium

Approach:
Use prefix and suffix products.

First pass:
Store product of all elements to the left.

Second pass:
Multiply by product of all elements to the right.

This avoids division and satisfies the O(n) requirement.

Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)
"""

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Left pass
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # Right pass
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

# ==========================================
# What I Learned:
#
# - Prefix products store multiplication from left side.
# - Suffix products store multiplication from right side.
# - Combining both gives product except self.
# - Avoids division and handles zeros correctly.
# ==========================================
