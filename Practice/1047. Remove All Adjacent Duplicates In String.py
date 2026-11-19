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

################################################################################

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

