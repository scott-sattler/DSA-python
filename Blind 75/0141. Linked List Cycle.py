"""
solutions:
    hash map using quick lookups
    fast-slow pointers (Floyd's)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while True:
            if not fast or not fast.next:
                return False

            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
