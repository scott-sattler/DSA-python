# naive
def brute_force(pattern: str, text: str):
    matches = list()
    p_i, s_i = 0, 0
    while s_i < len(text):
        # individual char match
        if pattern[p_i] != text[s_i]:
            s_i = (s_i - p_i) + 1  # backtrack (reset), increment
            p_i = 0
        # full pattern match
        elif p_i == len(pattern) - 1:
            matches.append((s_i - p_i))
            s_i = (s_i - p_i) + 1  # backtrack (reset), increment
            p_i = 0
        # increment
        else:
            s_i += 1
            p_i += 1

    return matches


# prefix length array
# text = 'abcabcg'
#       'a  b  c  a  b  c  g'
# pla = [0, 0, 0, 1, 2, 3, 0]

# def kmp(text: str, pattern: str):
#     # prefix length array
#     pla = list()
#     n = len(pattern)
#     length = 0
#     for i in range(n):
#         if i + 1 ==







test_cases = [
    # basic naive tests
    ('abc', 'abc', [0]),
    ('abc', 'abcd', [0]),
    ('dabc', 'abc', []),
    ('abc', 'aabcc', [1]),
    ('aaabc', 'abc', []),

    ('abc', 'abcbc', [0]),
    ('abc', 'abcabc', [0, 3]),
    ('aaa', 'aaaaaa', [0, 1, 2, 3]),
    ('baaac', 'aaaaaa', []),
    ('aaa', 'baaaaaac', [1, 2, 3, 4]),

    # kmp specific tests
    ('abcabcg', 'aaabcabcabcxabcabcg', [12]),

]


test_fns = {name: obj for name, obj in globals().copy().items() if callable(obj)}
for fn_name, each_fn in test_fns.items():
    for each_test in test_cases:
        print(each_test, end=' ')
        try:
            assert each_fn(each_test[0], each_test[1]) == each_test[2]
            print(fn_name, 'PASS')
        except AssertionError:
            print(fn_name, 'FAIL', end=' ')
            print(each_fn(each_test[0], each_test[1]))
            # assert brute_force(each_test[0], each_test[1]) == each_test[2]  # for easy debugging
