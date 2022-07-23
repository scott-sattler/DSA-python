"""
704. Binary Search
Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 10^4
    -10^4 < nums[i], target < 10^4
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""


class Solution:
    # first iterative attempt
    def search(self, nums: list[int], target: int) -> int:  # noqa static
        # binary search is O(log n)
        # get midpoint
        # compare midpoint with target
        #   if target larger, look right
        #   if target smaller, look left

        left_index = -1
        right_index = len(nums)

        while True:
            mid_index = left_index + ((right_index - left_index) // 2)
            mid_value = nums[mid_index]
            if mid_value == target:
                return mid_index
            if target > mid_value:
                left_index = mid_index
            else:  # target < mid_value
                right_index = mid_index

            if left_index + 1 == right_index:
                break

        return -1

    # second recursive attempt: with modified parameters
    # added optional None to preserve testing compatibility
    def third_attempt_search(self, nums: list[int], target: int, left: int | None = None, right: int | None = None) -> int:
        # get midpoint
        # return if midpoint is target
        # else recurse

        if left is None:
            left = -1
            right = len(nums)

        mid_index = left + ((right - left) // 2)
        mid_value = nums[mid_index]
        if mid_value == target:
            return mid_index

        if left + 1 == right:
            return -1

        if target > mid_value:
            left = mid_index
        else:  # target < mid_value
            right = mid_index

        return self.third_attempt_search(nums, target, left, right)

    # first recursive attempt: added additional constraint to not modify parameters
    def second_attempt_search(self, nums: list[int], target: int) -> int:
        # get midpoint
        # return if midpoint is target
        # else recurse

        # solve without modifying function parameters
        return_index = 0

        left_index = 0
        right_index = len(nums) - 1
        mid_index = (right_index - left_index) // 2
        mid_value = nums[mid_index]
        if mid_value == target:
            return mid_index

        if len(nums) == 1:
            return -1

        if target > mid_value:
            nums = nums[mid_index + 1:]
            return_index += mid_index + 1
        else:  # target < mid_value
            nums = nums[:mid_index]

        # basically just using recursion as for loop
        lol_gross = self.search(nums, target)

        if lol_gross > -1:
            return_index += lol_gross
        else:
            return_index = -1

        return return_index


class Test(Solution):
    tests = [
        # provided
        (
            ([-1, 0, 3, 5, 9, 12], 9),
            4
        ),
        (
            ([-1, 0, 3, 5, 9, 12], 2),
            -1
        ),


        (
            ([1], 0),
            -1
        ),
        (
            ([-1], 0),
            -1
        ),
        (
            ([0], 0),
            0
        ),
        (
            ([-1, 0, 1], 0),
            1
        ),
        (
            ([-10_000, 0, 10_000], 0),
            1
        ),
        (
            ([-11, -10, -9, -8], -8),
            3
        ),
        (
            ([-11, -10, -9, -8], -11),
            0
        ),
        (
            ([-11, -10, -9, -8], -10),
            1
        ),
        (
            ([-11, -10, -9, -8], -9),
            2
        ),
        (
            ([11, 12, 13, 14], 11),
            0
        ),
        (
            ([11, 12, 13, 14], 14),
            3
        ),
        (
            ([11, 12, 13, 14], 12),
            1
        ),
        (
            ([11, 12, 13, 14], 13),
            2
        ),
        (
            ([-100, 0, 100], 0),
            1
        ),
        (
            ([-1, 0], -1),
            0
        ),
        (
            ([-1, 0], 0),
            1
        ),
        (
            ([-10, 10], 0),
            -1
        ),
        (
            ([-10, 10], 10),
            1
        ),
        (
            ([-10, 10], -10),
            0
        ),

    ]

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.search(test_input[0], test_input[1])
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
