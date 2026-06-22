"""
Problem : Majority Element
Platform : LeetCode
Difficulty : Easy

Approach:
(Hash Map / Frequency Counting)

Initialize:
Create two variables:

- seen : a dictionary used to store the frequency of each element.
- n : stores the size of the array.

Traversal:

First Pass:
Traverse the array and count the frequency of each element.
Store the frequencies in the dictionary.

Second Pass:
Traverse the dictionary and find the element whose frequency
is greater than n/2.

Since the problem guarantees that a majority element exists,
return that element once found.

Time Complexity : O(n)
Space Complexity : O(n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        for key in seen:
            if seen[key] > n/2:
                return key
