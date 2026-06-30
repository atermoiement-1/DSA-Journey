"""
Problem : Plus One
Platform : LeetCode
Difficulty : Easy

Approach:
_____________

Number Conversion

Observation:
The given array represents a whole number where each element
corresponds to one digit.

Initialize:
Create:
- count : Stores the integer represented by the array.
- result : Stores the digits of the incremented number.

Traversal:

First Pass:
Traverse the array and convert the sequence of digits into
its corresponding integer.

Increment:
Add one to the constructed integer.

Second Pass:
Extract each digit of the updated number using the modulus
and integer division operations.
Store the digits in reverse order.

Finally:
Reverse the result list and return it.

Time Complexity : O(n)
Space Complexity : O(n)

Pattern Learned:
Number Conversion
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        for i in range(len(digits)):
            count = count * 10 + digits[i]
        count += 1
        result = []
        while count > 0:
            remainder = count % 10
            result.append(remainder)
            count //= 10
        return result[::-1]
        
