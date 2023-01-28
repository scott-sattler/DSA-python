"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""

from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # first attempt: previously solved
    # computational complexity:
    # space complexity:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # noqa: naming convention
        pass


# taken from 0019
class TestCase:
    def __init__(self, l1: ListNode, l2: ListNode, output: ListNode) -> None:
        self.l1 = l1
        self.l2 = l2
        self.output = output
        self.inp = (self.l1, self.l2)

    def __repr__(self):
        return str(hf.ll_to_non_ll(self.l1)) + str(hf.ll_to_non_ll(self.l2))


# taken from 0019
class Test:
    # preprocessing (boundaries)
    # None

    test_cases: list[TestCase] = [
        # provided
        TestCase(hf.create_ll([2, 4, 3]),
                 hf.create_ll([5, 6, 4]),
                 hf.create_ll([7, 0, 8])),

        TestCase(hf.create_ll([0]),
                 hf.create_ll([0]),
                 hf.create_ll([0])),

        TestCase(hf.create_ll([9, 9, 9, 9, 9, 9, 9]),
                 hf.create_ll([9, 9, 9, 9]),
                 hf.create_ll([8, 9, 9, 9, 0, 0, 0, 1])),

        # additional
        # TestCase(hf.create_ll([]),
        #          hf.create_ll([]),
        #          hf.create_ll([])),

        # failed

    ]

    def test_all(self, *include):
        """
        :param include: eg .test_all(0, 2, 5); or .test_all()
        :return: None
        """
        tests = self.test_cases
        s = Solution()

        pass_count = 0
        tests_failed = []
        for i, each_test in enumerate(tests):
            if len(include) > 0 and i not in include:
                continue
            test_input = each_test.inp  # <--- modify as needed
            # test_input_copy = hf.copy_ll()  # <--- for ll
            expected_output = each_test.output  # <--- modify as needed
            actual_output = s.addTwoNumbers(test_input[0], test_input[1])  # <--- fn name here
            # for ll
            # test_input_copy = hf.ll_to_non_ll(test_input_copy)
            test_input_rep = f"{hf.ll_to_non_ll(each_test.inp[0])}, {hf.ll_to_non_ll(each_test.inp[1])}"
            expected_output = hf.ll_to_non_ll(expected_output)
            actual_output = hf.ll_to_non_ll(actual_output)
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
                tests_failed.append(i)
            finally:

                print(f"  \t test_{i:03d}: {test_input_rep}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")

        tested = len(include) if len(include) > 0 else len(tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print()


# example usages
# Test().test_all(0, 2, 5); Test().test_all()
Test().test_all()
