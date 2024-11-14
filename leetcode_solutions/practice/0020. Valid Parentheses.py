'''
use stack
for each symbol
    if open symbol
        translate to compliment
        add to stack
    if closing symbol
        check stack for complement
        if not, return false
if stack empty, return true, else false


([{}])


'''


class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = list()

        for char in s:
            if char in hmap:  # default hmap.keys()
                stack.append(hmap[char])
            else:  # char not in hmap
                if not stack or stack[-1] != char:
                    return False
                stack.pop()

        if len(stack) < 1:
            return True
        return False
