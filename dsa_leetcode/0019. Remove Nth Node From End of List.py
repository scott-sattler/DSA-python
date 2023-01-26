"""
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz


Follow up: Could you do this in one pass?

"""
import copy
from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # second attempt: w/ follow-up; external reference
    # computational complexity: O(n)
    # space complexity: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # noqa: naming convention
        # two pointers approach
        return head

    # first attempt: with follow-up
    # computational complexity: O(n)
    # space complexity: O(n)
    def first_attempt_removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # noqa: naming convention
        # need to track each node
        # create list of node references
        current = head
        node_list = list()
        while current:
            node_list.append(current)
            current = current.next

        n = len(node_list) - n

        if len(node_list) == 1 and n == 0:
            return None

        if n == 0:
            return head.next

        if n == len(node_list) - 1:
            node_list[n - 1].next = None
        else:
            node_list[n - 1].next = node_list[n + 1]

        return head


# taken from 0841
class TestCase:
    def __init__(self, head: ListNode, n: int, output: ListNode) -> None:
        self.head = head
        self.n = n
        self.output = output
        self.inp = (self.head, self.n)

    def __repr__(self):
        return str(hf.ll_to_non_ll(self.head))


# taken from 0841
class Test:
    # preprocessing (boundaries)
    # None

    test_cases: list[TestCase] = [
        # provided
        TestCase(hf.create_ll([1, 2, 3, 4, 5]), 2, hf.create_ll([1, 2, 3, 5])),
        TestCase(hf.create_ll([1]), 1, hf.create_ll([])),
        TestCase(hf.create_ll([1, 2]), 1, hf.create_ll([1])),

        # additional


        # failed
        TestCase(hf.create_ll([1, 2]), 2, hf.create_ll([2])),

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
            test_input_copy = hf.copy_ll(each_test.head)  # <--- for ll
            expected_output = each_test.output  # <--- modify as needed
            actual_output = s.removeNthFromEnd(test_input[0], test_input[1])  # <--- fn name here
            # for ll
            test_input_copy = hf.ll_to_non_ll(test_input_copy)
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

                print(f"  \t test_{i:03d}: {test_input_copy} {each_test.n}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")

        tested = len(include) if len(include) > 0 else len(tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print()


# example usages
# Test().test_all(0, 2, 5); Test().test_all()
Test().test_all()

