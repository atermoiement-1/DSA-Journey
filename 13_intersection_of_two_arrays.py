"""
Problem : Intersection of Two Arrays
Platform : LeetCode
Difficulty : Easy

Approach:
(Set Intersection)

Initialize:
Create two sets:

- s1 : stores the unique elements from the first array.
- s2 : stores the unique elements from the second array.

Observation:
Sets automatically remove duplicate elements.

Traversal:
Convert both arrays into sets.

- Find the common elements using the intersection operator (&).
- Convert the resulting set back into a list and return it.

This approach efficiently finds all distinct elements
present in both arrays.

Time Complexity : O(n + m)
Space Complexity : O(n + m)

Pattern Learned:
Hash Set / Set Operations
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1 & s2)
