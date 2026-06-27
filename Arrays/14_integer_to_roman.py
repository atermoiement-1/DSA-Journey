"""
Problem : Integer to Roman
Platform : LeetCode
Difficulty : Medium

Approach:
_____________

Greedy Algorithm

Initialize:
Create two lists:
- values : Stores the Roman numeral values in descending order.
- symbols : Stores the corresponding Roman numeral symbols.

Also create:
- result : An empty string to store the final Roman numeral.

Traversal:
Iterate through every value in the values list.

For each value:
- While the given number is greater than or equal to the current value,
  append its corresponding Roman symbol to the result.
- Subtract the current value from the number.
- Continue this process until the number becomes smaller than the current value.

Repeat the same steps for all remaining values until the number becomes zero.

Finally, return the constructed Roman numeral.

Time Complexity : O(1)
Space Complexity : O(1)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        values  = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        result = ""
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]  
                num -= values[i]   
        return result
        
