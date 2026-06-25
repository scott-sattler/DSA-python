from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # noinspection all
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invertTree(_root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not _root:
                return None

            _root.left, _root.right = _root.right, _root.left

            _invertTree(_root.left)
            _invertTree(_root.right)

        _invertTree(root)
        return root
