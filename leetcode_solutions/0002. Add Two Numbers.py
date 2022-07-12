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


Notes:
    "Starting in Python 3.11 (to be released in late 2022), you'll be able to use Self as the return type."
    https://stackoverflow.com/a/70932112
"""

from __future__ import annotations
from typing import Optional
import helper_functions as hf


# Provided
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa (next shadows built-in name)
        self.val = val
        self.next = next


class Solution:
    # third attempt (after learning how to use linked lists)
    # unclear how to solve in O(n) without recursion
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # traverse linked list recursively
        #   concurrently add indices to linked list
        # >return created linked list

        linked_list = ListNode()
        if l1 is None and l2 is None:
            return None

        # simplifies None case
        first_list_digit = 0
        second_list_digit = 0
        l1_arg = None
        l2_arg = None

        if l1 is not None:
            first_list_digit = l1.val
            l1_arg = l1.next
        if l2 is not None:
            second_list_digit = l2.val
            l2_arg = l2.next

        # two-digit cases
        total = first_list_digit + second_list_digit
        if total > 9:
            linked_list.val = total - 10
            if l1_arg:
                l1.next.val += 1
            elif l2_arg:
                l2.next.val += 1
            else:
                linked_list.next = ListNode(1)
                return linked_list
        else:
            linked_list.val = total

        linked_list.next = self.addTwoNumbers(l1=l1_arg, l2=l2_arg)

        return linked_list

    # second attempt (combining iteration and recursion) was abandoned

    # first attempt
    # nested implies recursion
    def create_list(self, number: list) -> ListNode | None:  # 3.11 -> Self
        node = ListNode()
        if len(number) == 0:
            return None

        node.val = number.pop(0)
        node.next = self.create_list(number)
        return node

    # first attempt; O(n3)?
    def first_attempt_addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # iterate over each list serially
        #   multiply by order of magnitude
        #   add to subtotal
        # combine the two totals
        # reverse and construct linked list
        # >return linked list

        first_total = i = digit = 0
        while True:
            digit = (10 ** i) * l1.val
            l1 = l1.next
            first_total += digit
            i += 1
            if l1 is None:
                break

        second_total = i = digit = 0
        while True:
            digit = (10 ** i) * l2.val
            l2 = l2.next
            second_total += digit
            i += 1
            if l2 is None:
                break

        total = first_total + second_total

        return self.create_list([i for i in str(total)[::-1]])


class Test(Solution):
    tests = \
        {
            hf.list_to_dict_key(
                [[2, 4, 3], [5, 6, 4]],  # l1 l2 list input
                selector="two-nested"
            ):  [7, 0, 8],  # linked list output

            hf.list_to_dict_key(
                [[9, 9, 9], [9]],
                selector="two-nested"
            ):  [8, 0, 0, 1],

            hf.list_to_dict_key(
                [[9], [9]],
                selector="two-nested"
            ):  [8, 1],

            hf.list_to_dict_key(
                [[0], [0]],
                selector="two-nested"
            ):  [0],

            hf.list_to_dict_key(
                [[0], [1]],
                selector="two-nested"
            ):  [1],

            hf.list_to_dict_key(
                [[0, 1], [1]],
                selector="two-nested"
            ):  [1, 1],

            hf.list_to_dict_key(
                [[1], [0, 1]],
                selector="two-nested"
            ):  [1, 1],

            hf.list_to_dict_key(
                [[1], [0]],
                selector="two-nested"
            ):  [1],

            hf.list_to_dict_key(
                [[0 for i0 in range(99)] + [1], [0 for j0 in range(99)] + [1]],
                selector="two-nested"
            ):  [0 for k0 in range(99)] + [2],

            hf.list_to_dict_key(
                [[1 for i1 in range(100)], [1 for j1 in range(100)]],
                selector="two-nested"
            ):  [2 for k1 in range(100)],

        }

    def test_all(self) -> None:
        for each_test in self.tests.items():
            test_input = each_test[0]
            expected_output = hf.create_linked_list(each_test[1].copy())
            expected_output_num = ''.join([str(i) for i in each_test[1]])
            test_output = Solution().addTwoNumbers(
                l1=hf.create_linked_list(test_input[0]),
                l2=hf.create_linked_list(test_input[1])
            )
            test_output_num = ''.join([str(i) for i in hf.ll_to_non_ll(test_output)])
            try:
                # assert test_output == expected_output
                assert test_output_num == expected_output_num
                print(f"PASS \t {each_test}")
            except AssertionError:
                print(f"FAIL \t {each_test}\n"
                      f"\t test_output: \t\t {hf.ll_to_non_ll(test_output)}\n"
                      f"\t expected_output: \t {hf.ll_to_non_ll(expected_output)}")


Test().test_all()
