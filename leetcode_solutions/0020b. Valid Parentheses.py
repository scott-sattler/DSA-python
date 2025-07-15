class Solution:
    def isValid(self, s: str) -> bool:
        h_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for each in s:
            if each in '([{':
                stack.append(each)
            elif not stack:
                return False
            elif h_map[each] != stack.pop():
                return False

        return True if not stack else False