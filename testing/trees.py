from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        return

    @staticmethod
    def make_tree_iter(arr) -> Node:
        """ level order (from left to right) """
        head = Node(arr[0])
        queue = deque([head, head])
        for val in arr[1:]:
            last_paren = queue.popleft()
            next_child = Node(val)
            if not last_paren.left:
                last_paren.left = next_child
                queue.extend([last_paren.left, last_paren.left])
            else:
                last_paren.right = next_child
                queue.extend([last_paren.right, last_paren.right])
        return head

    def make_tree_rec(self, arr):
        """ binary search tree """
        if not arr:
            return None
        mid = len(arr) // 2
        node = Node(arr[mid])
        node.left = self.make_tree_rec(arr[:mid])
        node.right = self.make_tree_rec(arr[mid + 1:])
        return node


class Test:
    def __init__(self):
        return

    # preorder traversal
    def preorder(self, root):
        stack = list()
        self._preorder(root, stack)
        return stack

    def _preorder(self, node, stack):
        if not node:
            return

        stack.append(node.val)
        self._preorder(node.left, stack)
        self._preorder(node.right, stack)

    # inorder traversal
    def inorder(self, root):
        stack = list()
        self._inorder(root, stack)
        return stack

    def _inorder(self, node, stack):
        if not node:
            return

        self._inorder(node.left, stack)
        stack.append(node.val)
        self._inorder(node.right, stack)

    # level order (BFS) traversal
    @staticmethod
    def level_order(root):
        queue = deque([root])
        stack = list()
        while queue:
            curr = queue.popleft()
            if not curr:
                continue
            queue.extend([curr.left, curr.right])
            stack.append(curr.val)
        return stack

    def test(self):
        pass


tree_inorder = Tree().make_tree_iter([1, 2, 3, 4, 5, 6, 7, 8])
# tree_bst = Tree().make_tree_rec([4, 2, 5, 1, 6, 3, 7])
tree_bst = Tree().make_tree_rec([1, 2, 3, 4, 5, 6, 7])

# print(Test().preorder(tree))
print(Test().inorder(tree_bst))
print(Test().level_order(tree_inorder))
