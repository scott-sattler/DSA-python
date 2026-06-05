"""
traverse/serialize in any order
record nulls (preserve shape information)
compare

dfs:
preorder
root
left
right

inoder
left
root
right

postorder
left
right
root

bfs:
level-order
queue

time: O(n)
space: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _is_same_tree(root: Optional[TreeNode], record: list):
            if root is None:
                record.append(None)
                return root

            record.append(root.val)
            _is_same_tree(root.left, record)
            _is_same_tree(root.right, record)

        a = []
        _is_same_tree(p, a)

        b = []
        _is_same_tree(q, b)

        if a == b:
            return True
        return False
