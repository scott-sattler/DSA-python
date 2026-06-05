from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# noinspection PyPep8Naming
# noinspection PyMethodMayBeStatic
# noinspection PyShadowingNames
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # preorder
        def _isSameTree(p, q):
            if p.val != q.val:
                return False

            if p.left and q.left:
                _isSameTree(p.left, q.left)
            elif p.left or q.left:
                return False

            if p.right and q.right:
                _isSameTree(p.right, q.right)
            elif p.right or q.right:
                return False

            return True

        return _isSameTree(p, q)




