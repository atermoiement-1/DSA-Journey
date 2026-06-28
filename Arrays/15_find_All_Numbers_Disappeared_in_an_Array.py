"""
Problem : Find All Numbers Disappeared in an Array
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Hash Set

Observation:
The array should contain every number from 1 to n.
Any number from this range that is not present in the array
is considered missing.

Initialize:
Create:
- seen : A set containing all elements of the input array.
- new : A list to store the missing numbers.

Traversal:
Iterate through every number from 1 to n.

For each number:
- Check whether it exists in the seen set.
- If it is not present, append it to the result list.

Finally, return the list containing all missing numbers.

Time Complexity : O(n)
Space Complexity : O(n)

Pattern Learned:
Hash Set
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new = []
        seen = set(nums)
        for num in range(1, len(nums)+1):
            if num not in seen:
                new.append(num)
        return new
        
