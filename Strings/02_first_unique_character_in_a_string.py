"""
Problem : First Unique Character in a String
Platform : LeetCode
Difficulty : Easy

Approach:

Frequency Counting

Initialize:
Create one dictionary:
- seen : Stores the frequency of every character in the string.

First Pass:
Traverse the string once and count how many times each character appears.
Store the frequency of every character in the dictionary.

Second Pass:
Traverse the string again using the index.
For each character, check its frequency in the dictionary.
If the frequency is 1, return its index immediately since it is the first non-repeating character.

If no unique character exists, return -1.

Time Complexity : O(n)
Space Complexity : O(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1

        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i

        return -1
