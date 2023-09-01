"""
101. Symmetric Tree
Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str((self.val, self.left, self.right))


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:  # noqa: naming

        return self._is_symmetric(root.left, root.right)

    def _is_symmetric(self, node_left, node_right) -> bool:
        if not node_left and not node_right:
            return True

        if not node_left or not node_right:
            return False

        if node_left.val != node_right.val:
            return False

        return self._is_symmetric(node_left.left, node_right.right) and self._is_symmetric(node_left.right, node_right.left)


'''
            1
           / \
          /   \
         /     \
        /       \
       2         2
      / \       / \
     /   \     /   \
    4     5   5     4
   / \   / \ / \   / \
  3   2 1  0 0  1 2   3
  
'''  # noqa

h3_0 = TreeNode(3)
h3_1 = TreeNode(2)
h3_2 = TreeNode(1)
h3_3 = TreeNode(0)
h3_4 = TreeNode(0)
h3_5 = TreeNode(1)
h3_6 = TreeNode(2)
h3_7 = TreeNode(3)

h2_0 = TreeNode(4, h3_0, h3_1)
h2_1 = TreeNode(5, h3_2, h3_3)
h2_2 = TreeNode(5, h3_4, h3_5)
h2_3 = TreeNode(4, h3_6, h3_7)

# h2_0 = TreeNode(4)
# h2_1 = TreeNode(5)
# h2_2 = TreeNode(6)
# h2_3 = TreeNode(4)

h1_0 = TreeNode(2, h2_0, h2_1)
h1_1 = TreeNode(2, h2_2, h2_3)

root = TreeNode(1, h1_0, h1_1)


print(Solution().isSymmetric(root))




