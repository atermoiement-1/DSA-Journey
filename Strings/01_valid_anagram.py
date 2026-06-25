"""
Problem : Valid Anagram
Platform : LeetCode
Difficulty : Easy

Approach:
(Sorting)

Observation:
Two strings are anagrams if they contain the same characters
with the same frequency.

Initialize:
No extra data structures are required.

Validation:
- First, compare the lengths of both strings.
- If the lengths are different, they cannot be anagrams.

Traversal:
- Sort both strings alphabetically.
- Compare the characters at each index.
- If any character differs, return False.
- If all characters match, return True.

Time Complexity : O(n log n)
Space Complexity : O(n)

Pattern Learned:
Sorting
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
