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


# ASCII implementation
# with naive optimization(s)
def rabin_karp(pattern: str, text: str):
    matches = list()
    if len(pattern) > len(text):
        return []

    # get pattern hash
    p_hash = sum([ord(char) for char in pattern])

    # get leftmost text hash
    t_hash = sum([ord(text[i]) for i in range(0, len(pattern))])

    # compare first occurrence
    if t_hash == p_hash:
        # exact test
        if pattern == text[0:len(pattern)]:
            matches.append(0)

    i = 0
    upper = len(text) - len(pattern)
    while i < upper:
        # calculate substring and pattern hashes
        t_hash -= ord(text[i])
        t_hash += ord(text[i + len(pattern)])

        # compare hashes
        if t_hash == p_hash:
            # exact test
            if pattern == text[(i + 1):(i + 1 + len(pattern))]:
                matches.append(i + 1)

        # increment
        i += 1

    return matches


test_cases = [
    # pattern, text, leftmost match index

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

    #rabin-karp specific tests
    # not specific
    ('abc', 'aaabcabcc', [2, 5]),
    ('aaabc', 'aaabcabcc', [0]),
    ('aaaabc', 'aaabcabcc', []),
    ('aaac', 'aaabcabcc', []),
    ('aaab', 'aaabcabcc', [0]),
    ('bcc', 'aaabcabcc', [6]),
    ('bc', 'aaabcabcc', [3, 6]),

    ('bcd', 'ace', [])

]


test_fns = {name: obj for name, obj in globals().copy().items() if callable(obj)}
for fn_name, each_fn in list(test_fns.items())[1:]:  # specify fn here
    for each_test in test_cases[:]:  # specify test cases here
        print(each_test, end=' ')
        try:
            assert each_fn(each_test[0], each_test[1]) == each_test[2]
            print(fn_name, 'PASS')
        except AssertionError:
            print(fn_name, 'FAIL', end=' ')
            print(each_fn(each_test[0], each_test[1]))
            # assert brute_force(each_test[0], each_test[1]) == each_test[2]  # for easy debugging
