# time complexity: O(1)
def _ascii_map_base_10_lower(char: str, digits: int = 3) -> int:
    """ lowercase alpha ASCII char to base 10 mapping """
    # return 10 ** (ord(char) - 97)
    digits = 3  # 1_000
    return (10 ** digits) ** (ord(char) - 97)


# time complexity: O(n)
# supports arbitrary sized input
def map_ascii_lower(input_string: str) -> int:
    """ converts single string to map value, at minimum precision """
    # import math
    # n = len(input_string)
    # digits = (math.log10(n) // 1) + 1  # (// 1) -> math.floor()
    digits = len(str(len(input_string)))

    out = 0
    for c in input_string:
        out += _ascii_map_base_10_lower(c, digits)
    return out


# time complexity: O(n) with fixed size words
def convert_to_ints(input_list_of_strs: list[str]) -> list[int]:
    # find max size
    max_size = 0
    for s in input_list_of_strs:
        if len(s) > max_size:
            max_size = len(s)

    # import math
    # n = len(input_string)
    # digits = (math.log10(n) // 1) + 1  # (// 1) -> math.floor()
    digits = len(str(max_size))

    converted = list()
    for c in input_list_of_strs:
        converted.append(_ascii_map_base_10_lower(c, digits))
    return converted


if __name__ == '__main__':
    import traceback

    # todo: move to helper fns
    red = 91
    green = 92
    def colorify(color: int, text: str) -> str: return str(f'\x1b[{str(color)}m' + text + '\x1b[0m')

    tests = [
        ('a', 1),
        ('b', 1000),
        ('c', 1000000),
        ('abc', 1001001),
        ('cab', 1001001),
        ('bac', 1001001),
        ('dac', 1001000001),
        ('cad', 1001000001),

        ('aaa', 3),

        ('c' * 9, 9000000),
        ('c' * 10, 10000000),

        ('a' * 100, 100),
        ('a' * 100 + 'bb', 2100),

        ('z', 1000000000000000000000000000000000000000000000000000000000000000000000000000),
        ('z' * 10, 10000000000000000000000000000000000000000000000000000000000000000000000000000),
        ('z'*100, 100000000000000000000000000000000000000000000000000000000000000000000000000000),

        (('z' * 100) + 'aaabbb', 100000000000000000000000000000000000000000000000000000000000000000000000003003),
        (('z' * 100) + 'ababab', 100000000000000000000000000000000000000000000000000000000000000000000000003003),
        (('z' * 100) + 'bbbaaa', 100000000000000000000000000000000000000000000000000000000000000000000000003003),
    ]

    exceptions = list()
    def truncate(s): return s if len(s) < 11 else f"{s[:8]} ... {s[-3:]} len_{len(s)}"
    for test in tests:
        test_info = f"""{truncate(test[0])} -> {test[1]}"""
        try:
            assert map_ascii_lower(test[0]) == test[1]
            print(colorify(92, 'PASS'), test_info)
        except (BaseException,) as e:
            fail = colorify(91, 'FAIL')
            expected = colorify(92, test_info)
            actual = colorify(91, f"!= {map_ascii_lower(test[0])}")
            print(fail, expected, actual)
            data = "".join(traceback.format_exception(type(e), e, e.__traceback__))
            exceptions.append(data)

    print()
    for e in exceptions:
        # traceback.print_exception(e, file=sys.stdout)
        # traceback.print_exception(e, file=sys.stderr)
        print(colorify(91, e))
