"""
encodes using preorder traversal
data is encoded in UTF-8
data types are not preserved (not encoded)

this abomination was adapted from an abandoned implementation of a lossy binary
tree serializer that was limited to being used for Huffman coding (therefore,
not paralytically interesting, given superior Huffman header implementations)
"""

from __future__ import annotations
from dataclasses import dataclass


DELIMITER = ' '  # space
NULL_NODE = '0'
NON_NULL_NODE = '1'


@dataclass
class Node:
    data: any
    left: Node = None
    right: Node = None


def serialize_preorder(root: Node) -> str:
    def _serialize(node: Node, nodes: list[int], data: list[any]) -> None:
        if not node:
            return node_list.append(NULL_NODE)
        node_list.append(NON_NULL_NODE)
        data.append(node.data)
        _serialize(node.left, nodes, data)
        _serialize(node.right, nodes, data)

    node_list = []
    data_list = []
    _serialize(root, node_list, data_list)

    node_string = ''.join(str(n) for n in node_list)
    data_strings = list(map(str, data_list))
    data_string = f'{DELIMITER}'.join(
        ''.join(map(bin, bytearray(datum, encoding='utf_8')))
        for datum in data_strings
    )
    return node_string + DELIMITER + data_string


def deserialize_preorder(serialized_tree: str) -> None | Node:
    if not serialized_tree:
        return None

    data_offset = 0
    for e in serialized_tree:
        if e == DELIMITER:
            break
        data_offset += 1
    data_offset += 1

    decoded_data = []
    for datum in serialized_tree[data_offset:].split(DELIMITER):
        next_symbol = []
        for sub_symbol in datum[2:].split('0b'):
            next_symbol.append(chr(int(sub_symbol, 2)))
        decoded_data.append(''.join(next_symbol))

    decoded_data = decoded_data[::-1]  # O(n) mutation for O(1) pops

    def _deserialize(iter_nodes):
        def _construct_next():
            if not (next_node := next(iter_nodes, None)):
                return None

            if next_node == NULL_NODE:
                return None
            node = Node(decoded_data.pop())
            node.left = _construct_next()
            node.right = _construct_next()
            return node
        return _construct_next()

    nodes = iter(list(serialized_tree[:data_offset - 1]))
    return _deserialize(nodes)


if __name__ == '__main__':
    """ examples """
    root_ = Node(1)
    root_.right = Node('A')
    root_.right.left = Node(33)
    root_.right.left.right = Node('a')
    serialized_ = serialize_preorder(root_)
    print(serialized_)

    serialized_input_ = '101101000 0b110001 0b1000001 0b1100110b110011 0b1100001'
    deserialized_ = deserialize_preorder(serialized_input_)
    print(deserialized_)


class TestClass:
    @staticmethod
    def to_bin(datum) -> str:
        return ''.join(map(bin, bytearray(str(datum), encoding='utf_8')))

    def test_1(self):
        test_root = Node(1)
        expected = f'100 {self.to_bin(1)}'
        actual_serialized = serialize_preorder(test_root)
        assert actual_serialized == expected

    def test_2(self):
        test_root = Node(11)
        expected = f'100 {self.to_bin(11)}'
        actual_serialized = serialize_preorder(test_root)
        assert actual_serialized == expected

    def test_3(self):
        test_root = Node('1')  # ints not allowed
        input_ = f'100 {self.to_bin(1)}'
        actual_deserialized = deserialize_preorder(input_)
        assert actual_deserialized == test_root

    def test_4(self):
        test_root = Node('1')  # ints not allowed
        test_root.left = Node('2')
        input_ = f'11000 {self.to_bin(1)} {self.to_bin(2)}'
        actual_deserialized = deserialize_preorder(input_)
        assert actual_deserialized == test_root

    def test_5(self):
        test_root = Node('1')  # ints not allowed
        test_root.right = Node('2')
        input_ = f'101000 {self.to_bin(1)} {self.to_bin(2)}'
        actual_deserialized = deserialize_preorder(input_)
        assert actual_deserialized == test_root

    def test_6(self):
        test_root = Node('1')  # ints not allowed
        test_root.right = Node('A')
        test_root.right.left = Node('33')
        test_root.right.left.right = Node('a')
        input_ = f"101101000 {self.to_bin(1)} {self.to_bin('A')} {self.to_bin(33)} {self.to_bin('a')}"
        actual_deserialized = deserialize_preorder(input_)
        assert actual_deserialized == test_root
