"""
Problem : Longest Substring Without Repeating Characters
Platform : LeetCode
Difficulty : Medium

Approach:
(Sliding Window)

Initialize:

Create three variables:

- seen : stores the unique characters currently present in the sliding window.
- left : points to the start of the current window.
- maxi : stores the length of the longest valid substring found so far.

Traversal:

Traverse the string using a right pointer.

For each character:

- If the character already exists in the current window,
  shrink the window from the left until the duplicate is removed.

- Add the current character to the set.

- Update maxi with the maximum window size:

      right - left + 1

This ensures that the window always contains unique characters.

Time Complexity : O(n)
Space Complexity : O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxi = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            maxi = max(maxi, i-left+1)
        return maxi
