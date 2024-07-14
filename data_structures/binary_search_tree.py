import random


class BST:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __repr__(self):
        return str(self.in_order_rep())

    def __init__(self):
        self.root = None

    def in_order_rep(self) -> list:
        rep = list()
        node = self.root

        def in_order(curr, output):
            if not curr:
                return
            in_order(curr.left, output)
            rep.append(curr.val)
            in_order(curr.right, output)

        in_order(node, rep)
        return rep

    def insert(self, ins_val: int | float) -> None:
        node = self.Node(ins_val)
        if not self.root:
            self.root = node
            return
        self._hf_insert(node, self.root, None)

    def _hf_insert(self, node, curr, prev) -> None:
        if not curr:
            if node.val < prev.val:
                prev.left = node
            else:
                prev.right = node
        else:
            if node.val < curr.val:
                self._hf_insert(node, curr.left, curr)
            else:
                self._hf_insert(node, curr.right, curr)

    def search(self, find) -> bool:
        curr = self.root
        if not curr:
            return False
        return self._search_hf(self.root, find)

    def _search_hf(self, node, find) -> bool:
        if not node:
            return False

        if node.val == find:
            return True
        elif find < node.val:
            return self._search_hf(node.left, find)
        else:
            return self._search_hf(node.right, find)


if __name__ == '__main__':
    # test_list = [0, 9, 4, 2, 7, 1, 89, 3, 8, 6]
    test_lists = list()
    test_lists.append(random.choices([i for i in range(-100, 0)], k=10))
    test_lists.append(random.choices([i for i in range(0, 100)], k=10))
    test_lists.append(random.choices([i for i in range(-100, 100)], k=10))
    for test_list in test_lists:
        tree = BST()
        for value in test_list:
            tree.insert(value)
        print(tree)
        for value in test_list:
            print(tree.search(value), end=' ')
        print()

        for value in test_list:
            print(tree.search(value - 1) == ((value - 1) in test_list), end=' ')
        print()

        for value in test_list:
            print(tree.search(value + 1) == ((value + 1) in test_list), end=' ')
        print()

        for i in range(-10, 100):
            if i % 10 == 0:
                print()
            print(tree.search(i) == (i in test_list), end=' ')
        print('\n')
