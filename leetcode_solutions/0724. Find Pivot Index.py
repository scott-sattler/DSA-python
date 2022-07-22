"""
724. Find Pivot Index
Easy

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of
all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This
also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
        The pivot index is 3.
        Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
        There is no index that satisfies the conditions in the problem statement.

Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
        The pivot index is 0.
        Left sum = 0 (no elements to the left of index 0)
        Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
"""


class Solution:
    # second attempt: modified first
    # more performant and concise but potentially less clear/readable
    # time complexity: worst O(2n) -> O(n)
    # space complexity: constant -> O(1)
    def pivotIndex(self, nums: list[int]) -> int:  # noqa
        # sum array
        #   right is sum
        #   left is 0
        #   reasoning: leftmost pivot index
        # iterate given array rightward
        #   move right sum elements to left sum
        #   return index if equal
        #   readability: test is done between iterations

        left_sum = 0
        right_sum = sum(nums)

        for i in range(0, len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

    # first attempt
    # time complexity: worst O(2n) -> O(n)
    # space complexity: constant -> O(1)
    def firt_attempt_pivotIndex(self, nums: list[int]) -> int:  # noqa
        # sum array
        #   right is sum
        #   left is 0
        #   reasoning: leftmost pivot index
        # iterate given array rightward
        #   move right sum elements to left sum
        #   return index if equal

        left_sum = 0
        right_sum = sum(nums) - nums[0]

        for i in range(0, len(nums)):
            if i > 0:
                left_sum += nums[i - 1]
                right_sum -= nums[i]

            if left_sum == right_sum:
                return i

        return -1


class Test(Solution):
    tests = (
        (
            [1, 7, 3, 6, 5, 6],
            3
        ),
        (
            [1, 2, 3],
            -1
        ),
        (
            [2, 1, -1],
            0
        ),

        # edge cases
        (
            [0],
            0
        ),
        (
            [0, 0, 0, 0, 0],
            0
        ),
        (
            [3],
            0
        ),
        (
            [-5],
            0
        ),
        (
            [-5, 5],
            -1
        ),
        (
            [1, 1],
            -1
        ),

        # failed cases
        (
            [-1, -1, -1, -1, -1, 0],
            2
        ),

    )

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.pivotIndex(test_input)
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
            finally:

                print(f"  \t test_inp: {test_input}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")
        print(f'SUMMARY: TESTED {len(self.tests)} | PASSED {pass_count} | FAILED {len(self.tests) - pass_count}')


Test().test_all()
