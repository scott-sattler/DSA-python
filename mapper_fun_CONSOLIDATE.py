# time complexity: O(1)
def _ascii_map_base_10_lower(char: str) -> int:
    """ lowercase alpha ASCII char to base 10 mapping """
    return 10 ** (ord(char) - 97)


# time complexity: O(n)
def map_ascii_lower(input_string: str) -> int:
    out = 0
    for c in input_string:
        out += _ascii_map_base_10_lower(c)
    return out


if __name__ == '__main__':
    import traceback

    # todo: move to helper fns
    red = 91
    green = 92
    def colorify(color: int, text: str) -> str: return str(f'\x1b[{str(color)}m' + text + '\x1b[0m')

    tests = [
        ('abc', 111),
        ('cab', 111),
        ('bac', 111),
        ('dac', 1101),
        ('cad', 1101),

        ('aaa', 3),
    ]

    exceptions = list()
    for test in tests:
        test_info = f"""{test[0]} -> {test[1]}"""
        try:
            assert map_ascii_lower(test[0]) == test[1]
            print(colorify(92, 'PASS'), test_info)
        except (BaseException,) as e:
            print(colorify(91, 'FAIL'), test_info)
            exceptions.append("".join(traceback.format_exception(type(e), e, e.__traceback__)))

    print()
    for e in exceptions:
        # traceback.print_exception(e, file=sys.stdout)
        # traceback.print_exception(e, file=sys.stderr)
        print(colorify(91, e))
