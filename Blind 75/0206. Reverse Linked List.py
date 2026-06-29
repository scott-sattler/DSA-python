"""
1->2->3
^

None<-1

1->2->3
^  ^
1<-2->3
   ^  ^
1<-2<-3

N<-1<-2<-3  4->5->N
      ^  ^
N<-1<-2<-3  4->5->N
         ^  ^
N<-1<-2<-3<-4<-5->N
               ^  ^
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = head.next

        left.next = None

        while right is not None:
            next_node = right.next
            right.next = left

            left = right
            right = next_node

        return left
