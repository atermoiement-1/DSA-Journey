"""
Problem : Kids With the Greatest Number of Candies
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Maximum Comparison

Observation:
A child can have the greatest number of candies if,
after receiving all the extra candies, their total is
greater than or equal to the current maximum number of candies.

Initialize:
Create:
- maxi : Stores the maximum number of candies among all children.
- result : Stores whether each child can have the greatest number of candies.

Traversal:
Traverse through every child's candy count.

For each child:
- Add the extra candies to the current candy count.
- Compare the result with the maximum number of candies.
- If it is greater than or equal to the maximum,
  append True to the result list.
- Otherwise, append False.

Finally, return the result list.

Time Complexity : O(n)
Space Complexity : O(n)

Pattern Learned:
Maximum Comparison
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= maxi:
                result.append(True)
            else:
                result.append(False)

        return result
