"""
23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

Example 2:
    Input: lists = []
    Output: []

Example 3:
    Input: lists = [[]]
    Output: []

Constraints:

    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 10^4.

"""

from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # first attempt:
    # computational complexity:
    # space complexity (auxiliary):
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:  # noqa: naming convention
        merged_ll = ListNode()
        dummy = merged_ll

        min_pointer_index = True  # warning
        while min_pointer_index is not None:
            min_pointer = ListNode(val=10**5)  # bounds; float('inf') gave warning
            min_pointer_index = None  # warning

            # find next smallest value
            for i, each_ll in enumerate(lists):
                if each_ll is not None and each_ll.val < min_pointer.val:
                    min_pointer = each_ll
                    min_pointer_index = i

            if min_pointer_index is not None:
                new_head = min_pointer.next
                lists[min_pointer_index] = new_head
                merged_ll.next = min_pointer
                merged_ll = merged_ll.next

        return dummy.next


# taken from 0021
class TestCase:
    def __init__(self, lists: list[ListNode], output: ListNode) -> None:
        self.lists = lists
        self.output = output
        self.inp = (self.lists,)

    def __repr__(self):
        return str([hf.ll_to_non_ll(i) for i in self.lists])


# taken from 0021
class Test:
    import test_cases as tc
    # preprocessing (boundaries)
    # None

    test_cases: list[TestCase] = [
        # provided
        TestCase(
            [hf.create_ll(i) for i in [
                [1, 4, 5],
                [1, 3, 4],
                [2, 6],
            ]],
            hf.create_ll(
                [1, 1, 2, 3, 4, 4, 5, 6]
            )),

        TestCase(
                [],
            hf.create_ll(
                []
            )),

        TestCase(
                [hf.create_ll([])],
            hf.create_ll(
                []
            )),

        # additional
        # TestCase(
        #     [hf.create_ll(i) for i in [
        #         [],
        #         [],
        #     ]],
        #     hf.create_ll(
        #         []
        #     )),

        # failed
        TestCase(
            [hf.create_ll(i) for i in tc.failed_test_2],
            hf.create_ll(tc.failed_test_2_expected)),

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
            test_input_rep = str([hf.ll_to_non_ll(i) for i in each_test.inp[0]])  # for ll

            expected_output = each_test.output  # <--- modify as needed
            actual_output = s.mergeKLists(test_input[0])  # <--- fn name here
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
