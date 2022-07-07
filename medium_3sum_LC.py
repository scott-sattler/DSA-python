# prompt
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

NOTE: The Algoexpert problem has one additional assumption with the input array that every element will be distinct,
whereas the Leetcode version doesn't have that assumption.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
Example 2:
    Input: nums = []
    Output: []
Example 3:
    put: nums = [0]
    Output: []
    
Constraints:
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""


class Solution:
    # brutish
    def threeSum_n3(self, nums: list[int]) -> list[list[int]]:
        found_list = []
        # sort list
        nums = sorted(nums)
        # iterate over list
        for i in range(len(nums)):
            # for each element, look at next, look for complement
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        found = sorted([nums[i], nums[j], nums[k]])
                        if found not in found_list:
                            found_list.append(found)
                    if nums[i] + nums[j] + nums[k] > 0:
                        break
        return found_list

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        found_list = []
        hashset_nums = set(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (-1 * (nums[i] + nums[j])) in hashset_nums:
                    found = [nums[i], nums[j], -1 * (nums[i] + nums[j])]
                    found = sorted(found)
                    if found not in found_list:
                        found_list.append(found)

        return found_list



print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
