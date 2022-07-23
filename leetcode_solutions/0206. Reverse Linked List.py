"""
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa
        self.val = val
        self.next = next


class Solution:
    # first attempt
    # time complexity: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # create ll, backwards

        reversed_ll: ListNode | None = None
        linked_list = head

        while linked_list:
            reversed_ll = ListNode(linked_list.val, reversed_ll)
            linked_list = linked_list.next

        return reversed_ll

    # second attempt: in-place
    # much slower
    # time complexity: O(n)
    def second_attempt_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # reverse in-place by swapping references/'pointers'
        # initialize nodes: current, previous, next (empty)
        # loop
        #   get next node through current node link
        #   link current node to previous node
        #   assign previous node to current node
        #   assign current node to the next node

        previous_node: ListNode | None = None
        current_node: ListNode | None = head
        next_node: ListNode | None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        return previous_node


class Test(Solution):
    tests = [
        # provided
        [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1]
        ],
        [
            [1, 2],
            [2, 1]
        ],
        [
            [],
            []
        ],

    ]

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = hf.ll_to_non_ll(self.reverseList(hf.create_ll(test_input)))
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
