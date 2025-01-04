from __future__ import annotations
import heapq
from dataclasses import dataclass


# todo:
#  implement canonical Huffman code implementation
#  fix tree construction (hence, code assignment)
#  be more explict


@dataclass
class Node:
    char: str | None
    freq: int = 0
    left: Node = None
    right: Node = None

    """
    overriding comparators simplifies usage within heapq operations
    frequency ties are broken via ASCII decimal value (alphanumerically lexicographically)
    None nodes are always considered the right child, or b'1' on that level
    
    notes:
        given, n1 = 'a' and n2 = 'b', where n1.freq == n2.freq:
            n1 will appear lower in the priority queue, thus closer to the root
    """
    # def __lt__(self, other):
    #     # None nodes are never less than others (thus always rightmost children)
    #     if not self.char:
    #         return False
    #     if not other.char:
    #         return True
    #
    #     # priority queue ties are broken by inverting ascii value
    #     # level comparisons must be corrected on each level during tree construction
    #     if self.freq == other.freq:
    #         return ord(self.char) > ord(other.char)
    #
    #     # otherwise, sort by frequency
    #     return self.freq < other.freq
    #
    # def __gt__(self, other):
    #     # None nodes are always greater than others (thus always rightmost children)
    #     if not self.char:
    #         return True
    #     if not other.char:
    #         return False
    #
    #     # priority queue ties are broken by inverting ascii value
    #     # level comparisons must be corrected on each level during tree construction
    #     if self.freq == other.freq:
    #         return ord(self.char) < ord(other.char)
    #
    #     # otherwise, sort by frequency
    #     return self.freq > other.freq
    #
    # def __eq__(self, other):
    #     return self.freq == other.freq
    #
    # def __bool__(self):
    #     print('bool(self.char)', bool(self.char), self)
    #     if self is not None:
    #         return bool(self.char)
    #     return False


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

        priority_queue = [(f'{freq}{char}', Node(char, freq)) for char, freq in freq_map.items()]
        heapq.heapify(priority_queue)
        print(priority_queue)

        # build binary tree (bottom up)
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)[1]
            right = heapq.heappop(priority_queue)[1]

            # level correction hack (see comparator comments)
            if left.char is not None and right.char is not None:
                if left.freq < right.freq:
                    print('1: left.char', left.char, 'right.char', right.char)
                    left, right = right, left
                if left.freq == right.freq and left.char < right.char:
                    print('2: left.char', left.char, 'right.char', right.char)
                    left, right = right, left


            parent = Node(None, left.freq + right.freq, left, right)
            heapq.heappush(priority_queue, (f'{left.freq + right.freq}', parent))

        self.binary_tree = priority_queue[0][1]
        return self.binary_tree

    # O(n)
    def encode(self):
        if self.binary_tree is None:
            raise Exception('Binary Tree not yet constructed.')

        def preorder(node, code, encoding_map):
            if node is None:
                return
            if node.char is not None:
                encoding_map[node.char] = code.encode('ascii')
            preorder(node.left, code + '0', encoding_map)
            preorder(node.right, code + '1', encoding_map)

        encoded_map = {}
        preorder(self.binary_tree, '', encoded_map)
        self.encoded_map = encoded_map

        encoded = [encoded_map[symbol] for symbol in self.unencoded_symbols]

        # # todo: fix - broken
        # number = 0
        # for bits in encoded:
        #     number = (2 * number) + int(bits)
        # print(number, bin(number))
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
        return round(count / (len(self.encoded_map) * 8), 2)

    @staticmethod
    # O(n)
    def decode_with_prefix_map(encoded: list[bin], prefix_codes: dict):
        decoded = []
        for bits in encoded:
            decoded.append(prefix_codes[bits])
        return ''.join(decoded)


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    tests = [
        # dict(
        #     input_string='A DEAD DAD CED',
        #     expected_encoded_map={}),
        # dict(
        #     input_string='A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED',
        #     expected_encoded_map={}),
        # dict(
        #     input_string="abbccc",
        #     expected_encoded_map={'c': b'0', 'b': b'10', 'a': b'11'}),
        # dict(
        #     input_string="abbcc",
        #     expected_encoded_map={'b': b'0', 'c': b'10', 'a': b'11'}),
        dict(
            input_string="fdb",
            expected_encoded_map={'b': b'0', 'd': b'10', 'f': b'11'}),
        # dict(
        #     input_string='a' * 10 + 'b' + 'c' * 15 + 'd' * 7,
        #     expected_encoded_map={'b': b'00', 'd': b'01', 'a': b'10', 'c': b'11'}),
        # dict(
        #     input_string='abc',
        #     expected_encoded_map={'a': b'0', 'b': b'10', 'c': b'11'}),
        # dict(
        #     input_string='abcdef',
        #     expected_encoded_map={}),
    ]

    # inp_str = "My friend loves dragons. Dragons are friends. Friends are for food, dragons, are dragon."

    for test in tests:
        inp_str = test['input_string']
        exp_encoded_map = test['expected_encoded_map']

        huff = Huffman(inp_str)
        huff.construct()
        encoded_data = huff.encode()
        # print(huff.binary_tree)

        # prefix_codes_ = huff.prefix_codes()
        # print('prefix_codes_', prefix_codes_)

        # decoded_data = huff.decode_with_prefix_map(encoded_data, prefix_codes_)
        # print('decoded_data', decoded_data)

        # print(huff.calculate_efficiency())

        actual_encoded_map = huff.encoded_map
        print(actual_encoded_map == exp_encoded_map)
        print('exp_encoded_map', exp_encoded_map)
        print('huff.encoded_map', huff.encoded_map)

        print('huff.frequency_map', huff.frequency_map)
