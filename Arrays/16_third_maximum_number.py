"""
Problem : Third Maximum Number
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Three Maximum Tracking

Observation:
Maintain the three largest distinct numbers while traversing
the array only once.

Initialize:
Create three variables:

- l  : Stores the largest distinct number.
- sl : Stores the second largest distinct number.
- t  : Stores the third largest distinct number.

Initialize all three variables with negative infinity.

Traversal:
Traverse every element in the array.

For each element:

- Skip the element if it is already stored as one of the three maximum values.
- If the current element is greater than the largest value:
    - Shift the current largest to second largest.
    - Shift the current second largest to third largest.
    - Update the largest value.
- Else if the current element is greater than the second largest:
    - Shift the current second largest to third largest.
    - Update the second largest.
- Else if the current element is greater than the third largest:
    - Update the third largest.

After traversal:
- If a third distinct maximum exists, return it.
- Otherwise, return the largest element.

Time Complexity : O(n)
Space Complexity : O(1)

Pattern Learned:
Maximum Tracking
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = float('-inf')
        sl = float('-inf')
        t = float('-inf')
        for num in nums:
            if num in (l, sl, t):
                continue
            if num > l:
                t = sl
                sl = l
                l = num
            elif num > sl:
                t = sl
                sl = num
            elif num > t:
                t = num
        return t if t != float('-inf') else l
