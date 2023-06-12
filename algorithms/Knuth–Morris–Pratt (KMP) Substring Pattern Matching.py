# naive
def brute_force(pattern: str, string: str):
    matches = list()
    p_i, s_i = 0, 0
    while s_i < len(string):
        # individual char match
        if pattern[p_i] != string[s_i]:
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


test_cases = [
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

]

for each_test in test_cases:
    print(each_test, end=' ')
    try:
        assert brute_force(each_test[0], each_test[1]) == each_test[2]
        print('PASS')
    except AssertionError:
        print('FAIL', end=' ')
        print(brute_force(each_test[0], each_test[1]))
        # assert brute_force(each_test[0], each_test[1]) == each_test[2]  # for easy debugging




