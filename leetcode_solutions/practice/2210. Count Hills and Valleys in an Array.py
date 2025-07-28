class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0

        i = 0
        j = 2
        while j < len(nums):
            if nums[j] == nums[j - 1]:
                j += 1
                continue
            if nums[i] < nums[j - 1] and nums[j] < nums[j - 1]:
                count += 1
            elif nums[i] > nums[j - 1] and nums[j] > nums[j - 1]:
                count += 1
            i = j - 1
            j += 1

        return count
