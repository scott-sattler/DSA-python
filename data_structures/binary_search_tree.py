

class BST:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def in_order_rep(self):
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

    def insert(self, ins_val):
        node = self.Node(ins_val)
        if not self.root:
            self.root = node
            return

        curr = self.root
        parr = curr
        while True:
            # child is null
            if not curr:
                if ins_val > parr.val:
                    parr.right = node
                else:
                    parr.left = node
                return

            parr = curr
            if ins_val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

if __name__ == '__main__':
    tree = BST()
    test_list = [0, 9, 4, 2, 7, 1, 89, 3, 8, 6]
    for val in test_list:
        tree.insert(val)
    print(tree.in_order_rep())

