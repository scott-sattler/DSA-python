from __future__ import annotations
import heapq
from dataclasses import dataclass


# todo:
#  implement canonical Huffman code implementation



@dataclass
class Node:
    char: str | None
    freq: int = 0
    left: Node = None
    right: Node = None

    """
    overriding comparators simplifies usage within heapq operations
    frequency ties are broken via ASCII decimal value (alphanumerically lexicographically)

    notes:
        None nodes are always considered greater than, right child, or b'1'
        where (N1 < N2), N1 will appear lower in the tree 
    """
    def __lt__(self, other):
        if not self.char:
            return True
        if not other.char:
            return False
        if self.freq == other.freq:
            return ord(self.char) < ord(other.char)
        return self.freq < other.freq

    def __gt__(self, other):
        if not self.char:
            return False
        if not other.char:
            return True
        if self.freq == other.freq:
            return ord(self.char) > ord(other.char)
        return self.freq > other.freq

    def __eq__(self, other):
        return self.freq == other.freq


class Huffman:
    binary_tree: Node = None
    frequency_map: dict = None
    encoded_map: dict = {}

    def __init__(self, unencoded_symbols: str):
        self.unencoded_symbols = unencoded_symbols

    # O(n log n)
    def construct(self):
        # create priority queue of frequencies
        freq_map = {}
        for char in self.unencoded_symbols:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1
        self.frequency_map = freq_map

        priority_queue = [(Node(k, v)) for k, v in freq_map.items()]
        heapq.heapify(priority_queue)
        print(priority_queue)

        # build binary tree (bottom up)
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            parent = Node(None, left.freq + right.freq, left, right)
            heapq.heappush(priority_queue, parent)

        self.binary_tree = priority_queue[0]
        return self.binary_tree

    # O(n)
    def encode(self):
        if not self.binary_tree:
            raise Exception('Binary Tree not yet constructed.')

        def preorder(node, code, encoding_map):
            if not node:
                return
            if node.char is not None:
                encoding_map[node.char] = code.encode('ascii')
            preorder(node.left, code + '0', encoding_map)
            preorder(node.right, code + '1', encoding_map)

        encoded_map = {}
        preorder(self.binary_tree, '', encoded_map)
        self.encoded_map = encoded_map

        encoded = [encoded_map[symbol] for symbol in self.unencoded_symbols]
        number = 0
        for bits in encoded:
            number = (2 * number) + int(bits)
        print(number, bin(number))


        return encoded

    # O(n)
    def prefix_codes(self):
        if not self.encoded_map:
            raise Exception('Encoding map not yet constructed.')

        return {v: k for k, v in self.encoded_map.items()}

    def decode(self):
        ...

    # O(n)
    def calculate_efficiency(self):
        if not self.encoded_map:
            raise Exception('Encoding map not yet constructed.')
        count = sum([len(bits) for bits in self.encoded_map.values()])
        return round(count/(len(self.encoded_map)*8), 2)

    @staticmethod
    # O(n)
    def decode_with_prefix_map(encoded: list[bin], prefix_codes: dict):
        decoded = []
        for bits in encoded:
            decoded.append(prefix_codes[bits])
        return ''.join(decoded)


if __name__ == '__main__':
    # # noinspection SpellCheckingInspection
    # inp_str = "A DEAD DAD CED"
    # exp_out = [b'00', b'01', b'11', b'101', b'00', b'11', b'01', b'11', b'00', b'11', b'01', b'100', b'101', b'11']

    # # noinspection SpellCheckingInspection
    # inp_str = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
    # exp_out = [b'10', b'00', b'01', b'110', b'10', b'01', b'00', b'01', b'10', b'01', b'00', b'1110', b'110', b'01',
    #            b'110', b'01', b'00', b'10', b'00', b'1111', b'10', b'01', b'00', b'1111', b'10', b'1111', b'110', b'00',
    #            b'10', b'00', b'1111', b'110', b'10', b'01', b'110', b'01', b'00', b'10', b'1111', b'10', b'1110', b'10',
    #            b'00', b'1111', b'110', b'01']

    # inp_str = "abbccc"
    # exp_out = [b'10', b'11', b'11', b'0', b'0', b'0']

    # inp_str = "abbcc"
    # exp_out = [b'10', b'11', b'11', b'0', b'0']

    # inp_str = "fdb"
    # exp_out = [b'10', b'11', b'0']

    # inp_str = 'a'*10 + 'b' + 'c'*15 + 'd'*7
    # exp_out = []

    # inp_str = 'abc'
    # exp_out = []

    inp_str = 'abcdef'
    exp_out = []

    # inp_str = "My friend loves dragons. Dragons are friends. Friends are for food, dragons, are dragon."

    huff = Huffman(inp_str)
    huff.construct()
    encoded_data = huff.encode()
    # prefix_codes_ = huff.prefix_codes()
    # decoded_data = huff.decode_with_prefix_map(encoded_data, prefix_codes_)
    print(huff.binary_tree)
    print('encoded_data', encoded_data)
    # print('exp_out', exp_out)
    # print('prefix_codes_', prefix_codes_)
    # print('decoded_data', decoded_data)
    # print(encoded_data == exp_out)
    # print(huff.calculate_efficiency())

    print(huff.encoded_map)


