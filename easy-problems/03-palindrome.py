'''
-- 9. Palindrome Number --
Given an integer x, return true if x is a palindrome, and false otherwise.

Examples:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
* -231 <= x <= 231 - 1
'''

# Solution using strings
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# Solution without using strings
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        original_num = x

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original_num == reversed_num
