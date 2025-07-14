# O(n) time
# O(k) space (can reduce by adding code complexity)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sub = sum(nums[:k])  # O(k) space

        i = 1
        j = k
        curr_max = max_sub
        while j < len(nums):
            curr_max -= nums[i - 1]
            curr_max += nums[j]

            max_sub = max(curr_max, max_sub)

            i += 1
            j += 1

        return max_sub / k
