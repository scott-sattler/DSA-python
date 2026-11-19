class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for e in s:
            stack.append(e)

            if len(stack) < 2:
                continue

            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

        return ''.join(stack)
