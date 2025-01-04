"""
uses preorder traversal (encoding)
0s for non-leaf and 1s for leaf nodes

delimiter: █ (u"\u2588")
"""

from __future__ import annotations
from dataclasses import dataclass

DELIMITER = u"\u2588"  # █


@dataclass
class Node:
    data: any
    left: Node = None
    right: Node = None


def serialize_preorder(root: Node):
    def _serialize(node: Node, nodes: list[int], data: list[any]):
        if not node:
            return
        if node.left or node.right:
            nodes.append(0)
        else:
            nodes.append(1)
        data.append(node.data)
        _serialize(node.left, nodes, data)
        _serialize(node.right, nodes, data)

        return ''.join(
            e.__repr__() if type(e) is str
            else str(e)
            for e in (nodes + [DELIMITER] + data)
        )

    node_list = []
    data_list = []
    return _serialize(root, node_list, data_list)




if __name__ == '__main__':
    root_ = Node(1)
    root_.left = Node(2)
    root_.right = Node(3)
    print(root_)
    print(serialize_preorder(root_))

    root_ = Node('1')
    print(root_)
    print(serialize_preorder(root_))

    root_ = Node(1)
    root_.left = Node('2')
    root_.right = Node(3)
    print(root_)
    print(serialize_preorder(root_))
