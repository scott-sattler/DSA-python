"""
160. Intersection of Two Linked Lists
Easy

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two
linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
<https://assets.leetcode.com/uploads/2021/03/05/160_statement.png>

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):
    intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
    listA - The first linked list.
    listB - The second linked list.
    skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your
program. If you correctly return the intersected node, then your solution will be accepted.


Example 1:
<https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png>

Input:
    intersectVal = 8,
    listA = [4,1,8,4,5],
    listB = [5,6,1,8,4,5],
    skipA = 2,
    skipB = 3
Output:
    Intersected at '8'
Explanation:
    The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it
    reads as [4,1,8,4,5].
    From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes
    before the intersected node in B.
    - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd
    node in B) are different node references. In other words, they point to two different locations in memory, while the
    nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.


Example 2:
<https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png>

Input:
    intersectVal = 2,
    listA = [1,9,1,2,4],
    listB = [3,2,4],
    skipA = 3,
    skipB = 1
Output:
    Intersected at '2'
Explanation:
    The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the
    intersected node in A; There are 1 node before the intersected node in B.


Example 3:
<https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png>

Input:
    intersectVal = 0,
    listA = [2,6,4],
    listB = [1,5],
    skipA = 3,
    skipB = 2
Output:
    No intersection
Explanation:
    From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not
    intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation:
    The two lists do not intersect, so return null.


Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 10^4
    1 <= Node.val <= 10^5
    0 <= skipA < m
    0 <= skipB < n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

"""

# Definition for singly-linked list.
from typing import Optional
import helper_functions as hf


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:  # noqa: naming convention
        pass


# taken from 0002
class TestCase:
    def __init__(self,
                 intersectVal: int,
                 headA: ListNode,
                 headB: ListNode,
                 skipA: int,
                 skipB: int,
                 output: int | None) -> None:  # noqa: naming convention
        self.intersectVal = intersectVal
        self.headA = headA
        self.headB = headB
        self.skipA = skipA
        self.skipB = skipB
        self.output = output
        self.inp = (self.intersectVal, self.headA, self.headB, self.skipA, self.skipB)

    def __repr__(self):
        return str(hf.ll_to_non_ll(self.headA)) + str(hf.ll_to_non_ll(self.headB))


# taken from 0002
class Test:
    # preprocessing (boundaries)
    # None

    test_cases: list[TestCase] = [
        # provided
        TestCase(8,
                 hf.create_ll([4, 1, 8, 4, 5]),
                 hf.create_ll([5, 6, 1, 8, 4, 5]),
                 2,
                 3,
                 8),
        TestCase(2,
                 hf.create_ll([1, 9, 1, 2, 4]),
                 hf.create_ll([3, 2, 4]),
                 3,
                 1,
                 2),
        TestCase(0,
                 hf.create_ll([2, 6, 4]),
                 hf.create_ll([1, 5]),
                 3,
                 2,
                 None),

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
            # test_input_copy = hf.copy_ll()  # <--- for ll
            expected_output = each_test.output  # <--- modify as needed
            actual_output = s.getIntersectionNode(test_input[1], test_input[2])  # <--- fn name here
            # for ll
            # test_input_copy = hf.ll_to_non_ll(test_input_copy)
            # test_input_rep = f"{hf.ll_to_non_ll(each_test.inp[0])}, {hf.ll_to_non_ll(each_test.inp[1])}"
            test_input_rep = Warning("not implemented".upper())
            # expected_output = hf.ll_to_non_ll(expected_output)
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
