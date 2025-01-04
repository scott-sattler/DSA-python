from __future__ import annotations
import heapq
from dataclasses import dataclass

# todo:
#  implement canonical Huffman code
#  (efficiently) implement proper encoding (single binary string)
#  implement optimal serialized binary tree header or similar
#  review tree construction (hence, code assignment)
#  None node ties are arbitrary, and may be inconsistent without, e.g., a proper header

'''
references
https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1176/assnFiles/assign6/huffman-encoding-supplement.pdf

When we have choices among equally weighted nodes (such as in the first step 
choosing among the four characters with weight 1) picking a different two will 
result in a different, but still optimal, encoding. Similarly when combining 
two subtrees, it is as equally valid to put one of the trees on the left and 
the other on the right as it is to reverse them.

Remember that it is essential that you use the same tree to do both encoding 
and decoding of your files. Since each Huffman tree creates a unique encoding 
of a particular file, you need to ensure that your decoding algorithm generates 
the exact same tree, so that you can get back the file.

https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/388115265a456321c4a5d19dc9e05281_MIT6_046JS12_lec19.pdf

'''


@dataclass
class Node:
    char: str | None
    freq: int = 0
    left: Node = None
    right: Node = None

    """
    overriding comparators simplifies Node usage within heapq operations
    
    notes:
    frequency ties are broken via ASCII decimal value (alphanumerically lexicographically)
    None nodes are always considered the right child, or b'1' on a given level
    notice that, given, n1 = 'a' and n2 = 'b', where n1.freq == n2.freq:
        n1 will appear lower in the priority queue, thus closer to the root
    """
    def __lt__(self, other):
        # None nodes are never less than others (thus always rightmost children)
        if not self.char:
            return False
        if not other.char:
            return True
        # priority queue ties are broken by inverting ascii value (see notes above)
        if self.freq == other.freq:
            return ord(self.char) > ord(other.char)
        return self.freq < other.freq

    def __gt__(self, other):
        # handles null (None) non-leaf nodes
        # None nodes are always greater than others (thus always rightmost children)
        if not self.char:
            return True
        if not other.char:
            return False
        # priority queue ties are broken by inverting ascii value (see notes above)
        if self.freq == other.freq:
            return ord(self.char) < ord(other.char)
        # otherwise, sort by frequency
        return self.freq > other.freq


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

        priority_queue = [Node(char, freq) for char, freq in freq_map.items()]
        heapq.heapify(priority_queue)

        # build binary tree (bottom up)
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            parent = Node(None, left.freq + right.freq, left, right)
            heapq.heappush(priority_queue, parent)

        self.frequency_map = freq_map
        self.binary_tree = priority_queue[0]
        if len(self.frequency_map) == 1:
            self.binary_tree = Node(None, self.binary_tree.freq, self.binary_tree)
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
        return encoded

    # O(n)
    def prefix_codes(self):
        if not self.encoded_map:
            raise Exception('Encoding map not yet constructed.')
        return {v: k for k, v in self.encoded_map.items()}

    def decode(self, ):
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
    class Col:
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        RED = '\033[91m'
        END = '\033[0m'

    # noinspection SpellCheckingInspection
    tests = [
        # dict(
        #     input_string='A DEAD DAD CED',
        #     expected_encoded_map={}),
        # dict(
        #     input_string='A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED',
        #     expected_encoded_map={}),
        dict(
            input_string="abbccc",
            expected_encoded_map={}),
        dict(
            input_string="abbcc",
            expected_encoded_map={}),
        dict(
            input_string="fdb",
            expected_encoded_map={}),
        dict(
            input_string='a' * 10 + 'b' + 'c' * 15 + 'd' * 7,
            expected_encoded_map={}),
        dict(
            input_string='abc',
            expected_encoded_map={}),
        dict(
            input_string='abcdef',
            expected_encoded_map={}),
        dict(
            input_string='aaa',
            expected_encoded_map={'a': b'0'}),
        dict(
            input_string='z',
            expected_encoded_map={'z': b'0'}),
        dict(
            input_string='aaabbbcccdddeeefff',
            expected_encoded_map={}),
    ]

    for test in tests:
        inp_str = test['input_string']
        exp_encoded_map = test['expected_encoded_map']

        huff = Huffman(inp_str)
        huff.construct()
        encoded_data = huff.encode()
        prefix_codes_ = huff.prefix_codes()
        decoded_data = huff.decode_with_prefix_map(encoded_data, prefix_codes_)
        actual_encoded_map = huff.encoded_map

        print(f'input: {inp_str.__repr__()}')
        result = actual_encoded_map == exp_encoded_map
        col = Col.GREEN if result else Col.RED
        print(f'{col}{result}{Col.END}')

        print(huff.binary_tree)
        # print('huff.calculate_efficiency()', huff.calculate_efficiency())
        print(f'prefix_codes_: {prefix_codes_}')
        print(f'decoded_data: {decoded_data}')
        print(f'exp_encoded_map: {exp_encoded_map}')
        print(f'huff.encoded_map: {huff.encoded_map}')
        print(f'huff.frequency_map: {huff.frequency_map}')
        print()
