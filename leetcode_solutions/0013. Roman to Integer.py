"""
13. Roman to Integer
Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.

Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    lookup = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:  # noqa
        # solution:
        # iterate over string chars
        # look forward 1 for subtraction:
        #   when smaller value precedes a larger value
        # running total of lookup values
        # return: running total

        lookup = self.lookup
        i = total = 0
        while i < len(s):
            if i + 1 < len(s) and lookup[s[i]] < lookup[s[i + 1]]:
                total += lookup[s[i + 1]] - lookup[s[i]]
                i += 2
            else:
                total += lookup[s[i]]
                i += 1
        return total

    # second attempt: experimenting with improving clarity
    def second_attempt_romanToInt(self, s: str) -> int:  # noqa
        lookup = self.lookup
        i = total = 0
        while i < len(s):
            # boundary condition
            if i == len(s) - 1:
                total += lookup[s[i]]
                break

            current_value = lookup[s[i]]
            next_value = lookup[s[i + 1]]
            if current_value < next_value:
                total += next_value - current_value
                i += 2
            else:
                total += current_value
                i += 1

        return total

    # third attempt: experimenting with improving clarity
    def third_attempt_romanToInt(self, s: str) -> int:  # noqa
        lookup = self.lookup
        i = total = 0

        while i < len(s):
            current_value = lookup[s[i]]
            next_value = 0

            if i + 1 < len(s):
                next_value = lookup[s[i + 1]]

            if current_value < next_value:
                total += next_value - current_value
                i += 1
            else:
                total += current_value

            i += 1

        return total


class Test(Solution):
    tests = {
        # provided test cases
        'III': 3,
        'LVIII': 58,
        'MCMXCIV': 1994,

        # boundaries
        'I': 1,
        'MMMCMXCIX': 3999,
        # subtraction
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,

    }

    def test_all(self, test_all_solutions: bool = False) -> None:
        if test_all_solutions:
            test_functions = {k: v for k, v in Solution.__dict__.items() if 'romanToInt' in k}
        else:
            test_functions = {k: v for k, v in Solution.__dict__.items() if k == 'romanToInt'}

        for each_function in test_functions.items():
            print("TEST\t", each_function[0])
            for each_test in self.tests.items():
                input_value = each_test[0]
                output_value = each_function[1](Solution(), input_value)  # probably bad
                expected_out = each_test[1]
                try:
                    assert output_value == expected_out
                    print("PASS", end="")
                except AssertionError:
                    print("FAIL", end="")
                finally:
                    print(f"  \t test_inp: {input_value}\n"
                          f"\t\t expected_out: {expected_out}\n"
                          f"\t\t actual_out: {output_value}\n")


Test().test_all(False)
