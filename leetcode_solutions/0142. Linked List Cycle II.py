"""
142. Linked List Cycle II
Medium

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Note:   mutable, user defined objects are hashable in Python
        uses their id()
        unclear how to use id() to access object, like c pointer

        https://stackoverflow.com/a/56012972
        https://stackoverflow.com/a/66501227
"""

from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # follow-up attempt
    # time complexity: O(n)
    # space complexity: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # modifying first attempt approach
        # change the .val type to indicate visited status
        #   here, the int is put into a list
        # removing val changes would be O(n^2) time

        node = head
        while node:
            if isinstance(node.val, list):
                node.val = node.val[0]
                return node
            else:  # not visited
                node.val = [node.val]
                node = node.next

        return None

    # first attempt
    # time complexity: O(n)
    # space complexity: O(n)?
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # traverse ll
        #   check if visited
        #   record observed nodes

        node = head
        observed: dict[ListNode, any] = {}
        while node:
            observed_node: str | None = observed.get(node, None)
            if observed_node is not None:
                return node
            else:  # not in observed dict
                observed[node] = ''
                node = node.next

        return None

    # second attempt: id variation
    def second_attempt_detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        # traverse ll
        #   check if visited
        #   record observed nodes

        node = head
        observed: dict[id(ListNode), ListNode] = {}
        while node:
            observed_node: ListNode | None = observed.get(id(node), None)
            if observed_node is not None:
                return observed_node
            else:  # not in observed dict
                observed[id(node)] = node
                node = node.next
        return None


class Test(Solution):
    tests = (
        # provided
        (
            [[3, 2, 0, -4], 1],
            1
        ),
        (
            [[3, 2, 0, -4], 0],
            0
        ),
        (
            [[1], -1],
            None
        ),


        (
            [[-1, 3, 1, 5, 1], -1],
            None
        ),
        (
            [[0, 1, 2, 3, 4], 4],
            4
        ),
        (
            [[0, 1, 2, 3, 4], 0],
            0
        ),
        (
            [[0, 1, 2, 3, 4], 1],
            1
        ),
        (
            [[-6, -3, -1, 0, 1], 4],
            4
        ),

        (
            [[1, 2], 0],
            0
        ),

    )

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0][0]
            hidden_input = each_test[0][1]  # loops at
            expected_output = each_test[1]

            # test <-> solution format conversions: list[int]/int/None <-> ListNode
            looped_ll = hf.create_looped_ll(test_input, hidden_input)
            actual_output = self.detectCycle(looped_ll)
            actual_output = hf.get_depth_of_ll_node(looped_ll, actual_output)  # convert to testing format
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
            finally:

                print(f"  \t test_inp: {test_input}\n"
                      f"\t\t hidn_inp: {hidden_input}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")
        print(f'SUMMARY: TESTED {len(self.tests)} | PASSED {pass_count} | FAILED {len(self.tests) - pass_count}')


Test().test_all()
