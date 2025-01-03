class Huffman:
    def __init__(self):
        ...


    def encode(self, unencoded):
        ...


    def decode(self, encoded):
        ...


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    inp_str = "A DEAD DAD CED"

    exp_out = [b'00', b'01', b'11', b'101', b'00', b'11', b'01', b'11', b'00', b'11', b'01', b'100', b'101', b'11']

    actual_out = Huffman().encode(inp_str)
