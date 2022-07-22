"""
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true

Constraints:
    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ascii character.
"""


class Solution:
    # second attempt
    #   time: O(n + m)
    #   space:
    def isIsomorphic(self, s: str, t: str) -> bool:  # noqa
        hash_map: dict = {}
        used_set: dict = {}

        for i in range(0, len(s)):
            s_char = s[i]
            t_char = t[i]
            if not hash_map.get(s_char):
                if t_char in used_set:
                    return False
                hash_map[s_char] = t_char
                used_set[t_char] = ''
            elif hash_map[s_char] != t_char:
                return False

        return True

    # first attempt: lazy attempt
    # failed to carefully read problem
    def first_attempt_isIsomorphic(self, s: str, t: str) -> bool:  # noqa
        # count occurrences
        # compare counts

        bucket_s: dict = {}
        bucket_t: dict = {}

        for each_char in s:
            if bucket_s.get(each_char):
                bucket_s[each_char] += 1
            else:
                bucket_s[each_char] = 1

        for each_char in t:
            if bucket_t.get(each_char):
                bucket_t[each_char] += 1
            else:
                bucket_t[each_char] = 1

        s_bucket: list = list(bucket_s.values())
        t_bucket: list = list(bucket_t.values())

        for i in range(0, len(bucket_s)):
            if s_bucket[i] != t_bucket[i]:
                return False

        return True


class Test(Solution):
    tests = {
        # provided
        ('egg', 'add'):
        True,
        ('foo', 'bar'):
        False,
        ('paper', 'title'):
        True,

        ('a', 'b'):
        True,
        ('a', 'a'):
        True,
        ('aa', 'ab'):
        False,
        ('3', '4'):
        True,

        # failed
        ("bbbaaaba", "aaabbbba"):
        False,
        ("badc", "baba"):
        False


    }

    def test_all(self):
        pass_count = 0
        for each_test in self.tests.items():
            test_input_1, test_input_2 = each_test[0][0], each_test[0][1]
            expected_output = each_test[1]
            actual_output = self.isIsomorphic(test_input_1, test_input_2)
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
            finally:

                print(f"  \t test_inp: {each_test[0]}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")
        print(f'SUMMARY: TESTED {len(self.tests)} | PASSED {pass_count} | FAILED {len(self.tests) - pass_count}')


Test().test_all()
