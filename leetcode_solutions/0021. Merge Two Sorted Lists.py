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
    def __init__(self, val=0, next=None):  # noqa
        self.val = val
        self.next = next


class Solution:
    # first attempt
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        merged = ListNode()
        merged_head = merged
        node1 = list1
        node2 = list2

        while True:
            increment_node1 = False
            increment_node2 = False

            if node1 and node2:
                if node1.val < node2.val:
                    increment_node1 = True
                else:  # node1.val < node2.val:
                    increment_node2 = True
            elif node1:
                increment_node1 = True
            elif node2:
                increment_node2 = True
            else:
                break

            if increment_node1:
                merged.next = ListNode(node1.val, None)
                node1 = node1.next
            elif increment_node2:
                merged.next = ListNode(node2.val, None)
                node2 = node2.next
            merged = merged.next

        return merged_head.next


class Test(Solution):
    tests = [
        # provided
        (
            ([1, 2, 4], [1, 3, 4]),
            [1, 1, 2, 3, 4, 4]
        ),
        (
            ([], []),
            []
        ),
        (
            ([], [0]),
            [0]
        ),


        (
            ([0], []),
            [0]
        ),
        (
            ([0, 0], []),
            [0, 0]
        ),
        (
            ([], [0, 0]),
            [0, 0]
        ),
        (
            ([0, 0, 0, 1, 10, 20], [0, 0, 0, 1, 10, 20]),
            [0, 0, 0, 0, 0, 0, 1, 1, 10, 10, 20, 20]
        ),
        (
            ([1, 2, 3, 4], [1, 2, 3]),
            [1, 1, 2, 2, 3, 3, 4]
        ),
        (
            ([1, 2, 3], [1, 2, 3, 4]),
            [1, 1, 2, 2, 3, 3, 4]
        ),
        (
            ([0, 0, 0], []),
            [0, 0, 0]
        ),
        (
            ([], [0, 0, 0]),
            [0, 0, 0]
        ),
        (
            ([1, 2, 3], [4, 5, 6]),
            [1, 2, 3, 4, 5, 6]
        ),
        (
            ([-2, -1, 3], [4, 5, 6]),
            [-2, -1, 3, 4, 5, 6]
        ),
        (
            ([-2, -1, 0], [-6, -5, -5]),
            [-6, -5, -5, -2, -1, 0]
        ),
        (
            ([-2, -1], [-6]),
            [-6, -2, -1]
        ),
        (
            ([], [-6]),
            [-6]
        ),
        (
            ([], [-100]),
            [-100]
        ),
        (
            ([100], [-100]),
            [-100, 100]
        ),
        (
            ([-100], [100]),
            [-100, 100]
        ),
        (
            ([0], [100]),
            [0, 100]
        ),
        (
            ([0], [-100]),
            [-100, 0]
        ),

        (
            ([-1] * 25, [1] * 25),
            [-1] * 25 + [1] * 25
        ),
        (
            ([0] * 25, [0] * 25),
            [0] * 50
        ),

    ]

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0]
            expected_output = each_test[1]
            list1 = hf.create_ll(test_input[0])
            list2 = hf.create_ll(test_input[1])
            actual_output = hf.ll_to_non_ll(self.mergeTwoLists(list1, list2))
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
            finally:
                formatted_list1 = hf.print_verbose_ll(list1, get_string=True).replace('List', '\t\t\t\tList')
                formatted_list2 = hf.print_verbose_ll(list2, get_string=True).replace('List', '\t\t\t\tList')
                print(f"  \t test_inp: {test_input}\n"
                      f"\t\t\t list1: {formatted_list1}\n" 
                      f"\t\t\t list2: {formatted_list2}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")
        print(f'SUMMARY: TESTED {len(self.tests)} | PASSED {pass_count} | FAILED {len(self.tests) - pass_count}')


Test().test_all()
