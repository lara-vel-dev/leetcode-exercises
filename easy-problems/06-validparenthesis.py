'''
-- 20. Valid Parentheses --
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every close bracket has a corresponding open bracket of the same type.

Examples:
Input: s = "()"
Output: true

Input: s = "(]"
Output: false

Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in parenthesis_map:
                if stack and stack[-1] == parenthesis_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
