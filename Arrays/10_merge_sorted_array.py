"""
Problem : Merge Sorted Array
Platform : LeetCode
Difficulty : Easy

Approach:
(Three Pointer Technique)

Initialize:
Create three pointers:

- i : points to the last valid element in nums1.
- j : points to the last element in nums2.
- k : points to the last position in nums1 where the next largest element should be placed.

Traversal:

Compare the elements at i and j.

- Place the larger element at position k.
- Move the corresponding pointer backward.
- Move k backward after every placement.

Since nums1 has extra space at the end,
the array is filled from right to left to avoid overwriting
elements that have not been processed yet.

After one array is exhausted,
copy any remaining elements from the other array.

Time Complexity : O(m + n)
Space Complexity : O(1)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m-1, n-1, m+n-1
        while(i >= 0 and j >= 0):
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            
        while i >= 0:
            nums1[k] = nums1[i]
            i-= 1
            k-= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j-= 1
            k-= 1
