"""
Problem : Squares of a Sorted Array
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Square and Sort

Observation:
The array is sorted, but squaring negative numbers may change
their relative order. Therefore, after squaring every element,
the resulting array must be sorted again.

Initialize:
Create:
- squares : Stores the square of every element.

Traversal:
Traverse every element in the array.

For each element:
- Calculate its square.
- Append the squared value to the squares list.

After traversal:
- Sort the squared values.
- Return the sorted list.

Time Complexity : O(n log n)
Space Complexity : O(n)

Pattern Learned:
Sorting
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for i in nums:
            squares.append(i**2)
        sortt = sorted(squares)
        return sortt
