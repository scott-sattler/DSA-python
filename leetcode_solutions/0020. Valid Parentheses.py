"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    # first attempt
    def isValid(self, s: str) -> bool: # noqa
        lookup = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for each_char in s:
            lookup_val = lookup.get(each_char)
            if lookup_val:
                stack.append(lookup_val)
            elif len(stack) and stack.pop(-1) == each_char:
                continue
            else:
                return False

        if len(stack):
            return False

        return True


class Test(Solution):
    pass
