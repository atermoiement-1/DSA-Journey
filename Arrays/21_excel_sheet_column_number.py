"""
Problem : Excel Sheet Column Number
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Base-26 Conversion

Observation:
Excel column titles follow a Base-26 numbering system where:

A → 1
B → 2
...
Z → 26
AA → 27
AB → 28

To convert the column title into its corresponding number,
multiply the current result by 26 before adding the value of
the current character.

Initialize:
Create:
- result : Stores the decimal equivalent of the Excel column title.

Traversal:
Traverse each character in the string.

For each character:
- Multiply the current result by 26.
- Convert the character into its alphabetical position
  using the ASCII values.
- Add the converted value to the result.

Finally, return the computed column number.

Time Complexity : O(n)
Space Complexity : O(1)

Pattern Learned:
Base Conversion
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result
