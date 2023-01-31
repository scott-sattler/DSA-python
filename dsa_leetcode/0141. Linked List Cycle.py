"""
141. Linked List Cycle
Easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note
that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.


Constraints:
    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?

"""

from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # first attempt: previously solved
    # time complexity:
    # space complexity (auxiliary):
    def hasCycle(self, head: Optional[ListNode]) -> bool:  # noqa: naming convention
        pass


# taken from 0023
class TestCase:
    def __init__(self, ll_list: list, pos: int, output: bool) -> None:
        self.ll_list = ll_list
        self.pos = pos
        self.output = output
        self.inp = (hf.create_looped_ll(self.ll_list, self.pos), self.pos)

    def __repr__(self):
        return str(self.ll_list)


# taken from 0023
class Test:
    import test_cases as tc
    # preprocessing (boundaries)
    # None

    test_cases: list[TestCase] = [
        # provided
        TestCase(
            [3, 2, 0, -4],
            1,
            True),
        TestCase(
            [1, 2],
            0,
            True),
        TestCase(
            [1],
            -1,
            False),

        # additional

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

            # modify as needed: string representation of input
            test_input_rep = str(each_test.ll_list) + ', ' + str(each_test.pos)  # <--- modify as needed

            expected_output = each_test.output  # <--- modify as needed
            actual_output = s.hasCycle(test_input[0])  # <--- fn name here

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
