"""
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

"""

from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # noqa: naming convention
        pass


# taken from 0002 (not most recent)
class TestCase:
    def __init__(self, list1: ListNode, list2: ListNode, output: ListNode) -> None:
        self.list1 = list1
        self.list2 = list2
        self.output = output
        self.inp = (self.list1, self.list2)

    def __repr__(self):
        return str(hf.ll_to_non_ll(self.list1)) + str(hf.ll_to_non_ll(self.list2))


# taken from 002 (not most recent)
class Test:
    # preprocessing (boundaries)
    # None

    test_cases: list[TestCase] = [
        # provided
        TestCase(hf.create_ll([1, 2, 4]),
                 hf.create_ll([1, 3, 4]),
                 hf.create_ll([1, 1, 2, 3, 4, 4])),
        TestCase(hf.create_ll([]),
                 hf.create_ll([]),
                 hf.create_ll([])),
        TestCase(hf.create_ll([]),
                 hf.create_ll([0]),
                 hf.create_ll([0])),

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

            # test_input_copy = hf.copy_ll(each_test.inp)  # <--- for ll
            # test_input_copy = hf.ll_to_non_ll(test_input_copy[0])  # LL to list
            test_input_rep = f"{hf.ll_to_non_ll(each_test.inp[0])}, {hf.ll_to_non_ll(each_test.inp[1])}"  # for ll

            expected_output = each_test.output  # <--- modify as needed
            actual_output = s.mergeTwoLists(test_input[0], test_input[1])  # <--- fn name here
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
