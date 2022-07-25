"""
876. Middle of the Linked List
Easy

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100
"""

from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # first attempt: two pointers
    # time complexity: O(n)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # traverse ll
        #   record observed
        # calculate median
        # hash lookup

        hash_lookup: dict = {}

        i = 0
        while head:
            hash_lookup[i] = head

            head = head.next
            i += 1

        median_node = i // 2  # len(ll) // 2 -> rightmost on even

        return hash_lookup[median_node]


class Test(Solution):
    tests = (
        # provided
        (
            [1, 2, 3, 4, 5],
            [3, 4, 5]
        ),
        (
            [1, 2, 3, 4, 5, 6],
            [4, 5, 6]
        ),


        (
            [3],
            [3]
        ),
        (
            [4, 3, 2, 1, 5, 3, 7, 8, 100, 99, 98, 45],
            [7, 8, 100, 99, 98, 45]
        ),
        (
            [4, 3, 2, 1, 5, 3, 7, 8, 100, 99, 98],
            [3, 7, 8, 100, 99, 98]
        ),


    )

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = hf.ll_to_non_ll(self.middleNode(hf.create_ll(test_input)))
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
