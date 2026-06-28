"""
Problem : Running Sum of 1d Array
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Prefix Sum (In-place)

Observation:
The running sum at any index is obtained by adding the current
element with the running sum of the previous element.

Traversal:
Start traversing the array from index 1.

For each element:
- Add the previous element's running sum to the current element.
- Store the updated value back in the same array.

Since each position stores the running sum of all previous
elements, the original array itself becomes the result.

Finally, return the modified array.

Time Complexity : O(n)
Space Complexity : O(1)

Pattern Learned:
Prefix Sum
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
