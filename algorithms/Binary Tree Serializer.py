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


def serialize_preorder(root: Node) -> str:
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

    node_list = []
    data_list = []
    _serialize(root, node_list, data_list)
    return ''.join(
        e.__repr__() if type(e) is str
        else str(e)
        for e in (node_list + [DELIMITER] + data_list)
    )


def deserialize_preorder(serialized_tree: str) -> None | Node:
    if not serialized_tree:
        return None

    data_ptr = 0
    for e in serialized_tree:
        if e == DELIMITER:
            data_ptr += 2
            break
        data_ptr += 1

    stack = []  # unnecessary, but fun
    root = ptr = Node(None)
    for symbol in serialized_tree:
        if symbol == "'":
            if not stack:
                stack.append(symbol)
            else:
                stack.append(symbol)
                string = "".join(stack)
        elif symbol == '0':
            if not ptr.left:
                parent.left = Node(serialized_tree[data_ptr])








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
