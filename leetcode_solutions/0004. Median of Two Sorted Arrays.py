"""
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from __future__ import annotations

import math
import random as rdm

"""
Notes:

binary search is also known as: half-interval search, logarithmic search, or binary chop
https://en.wikipedia.org/wiki/Binary_search_algorithm
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:  # noqa
        pass


class Test(Solution):
    first_list_elements = rdm.randint(0, 1_000)
    second_list_elements = rdm.randint(1, 2_000 - first_list_elements)

    tests = \
        {
            str([
                [1, 3],
                [2]
            ]): 2.00000,

            str([
                [1, 2],
                [3, 4]
            ]): 2.50000,

            str([
                [1],
                [0]
            ]): 0.5,

            str([
                [1, 2, 3],
                [1, 2, 3]
            ]): 2.0,

            str([
                [1, 1, 1],
                [2, 2, 2]
            ]): 1.5,

            str([
                [1, 1, 1, 1, 1],
                [5]
            ]): 1.0,

            str([
                [1, 1, 1, 1, 1, 1, 1, 1],
                [5, 5, 5]
            ]): 1.0,

            # str([
            #         sorted(rdm.randint(0, 1_000) for i in range(first_list_elements)),
            #         sorted(rdm.randint(0, 1_000) for j in range(second_list_elements))
            #     ]): None,

            str([
                [5, 7, 7, 16, 19, 19, 19, 25, 45, 46, 49, 53],
                [0, 1, 3, 3, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7]
            ]): 6.0,

            str([
                [1, 3, 4, 7, 8,     16, 18, 19, 25, 45,     46, 49, 53],
                [0, 1, 2, 3, 4,     5, 6, 7, 8, 9,          10, 11, 12]
            ]): 8.0,

            str([
                [1, 3, 4, 6, 7,     16, 18, 19, 25, 45,     46, 49, 53],
                [0, 1, 2, 3, 4,     5, 6, 7, 7, 9,          10, 11, 12]
            ]): None,  # 7.0

        }

    # tests = {k: v for k, v in tests.items() if v == 6.0}
    # tests = {k: v for k, v in tests.items() if v == 2.0}
    # tests = {k: v for k, v in tests.items() if v == 8.0}
    # tests = {k: v for k, v in tests.items() if v is None}
    # tests = {k: v for k, v in tests.items() if v == 2.5}
    tests = {k: v for k, v in tests.items() if v == 1.0}

    @staticmethod
    # informally verified for correctness
    def get_answer(nums1: list[int], nums2: list[int]) -> float:
        brute_list = sorted(nums1 + nums2)

        def median(nums) -> float:
            if len(nums) % 2 == 0:
                nums_median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
            else:
                nums_median = nums[len(nums) // 2]
            return nums_median

        return median(brute_list)

    def test_all(self) -> None:
        for each_test in self.tests.items():
            test_input = eval(each_test[0])  # safe: ast.literal_eval
            test_output = self.findMedianSortedArrays(nums1=test_input[0], nums2=test_input[1])
            expected_output = each_test[1]
            if each_test[1] is None:
                expected_output = self.get_answer(nums1=test_input[0], nums2=test_input[1])
            try:
                assert test_output == expected_output
                print("PASS", end="")
            except AssertionError:
                print("FAIL", end="")
            finally:
                print(f"  \t test_inp: {test_input[0]}\n"
                      f"\t\t test_inp: {test_input[1]}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {test_output}\n")


Test().test_all()
