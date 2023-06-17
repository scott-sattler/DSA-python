# ASCII implementation
# with naive optimization(s)

def rabin_karp(text: str, pattern: str):
    # iterate over string
    # only add first, remove last (sliding window)
    # compare substring hash to pattern hash
    pass


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

    #rabin-karp specific tests


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
