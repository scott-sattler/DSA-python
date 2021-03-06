"""
8. String to Integer (atoi)
Medium

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi
function).

The algorithm for myAtoi(string s) is as follows:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it
    is either. This determines if the final result is negative or positive respectively. Assume the result is positive
    if neither is present.
    3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of
    the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer
    is 0. Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it
    remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than
    2^31 - 1 should be clamped to 2^31 - 1.
    6. Return the integer as the final result.

Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:
    Input: s = "42"
    Output: 42
    Explanation: The underlined characters are what is read in, the caret is the current reader position.
        Step 1: "42" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "42" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "42" ("42" is read in)
                   ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:
    Input: s = "   -42"
    Output: -42
    Explanation:
        Step 1: "   -42" (leading whitespace is read and ignored)
                    ^
        Step 2: "   -42" ('-' is read, so the result should be negative)
                     ^
        Step 3: "   -42" ("42" is read in)
                       ^
        The parsed integer is -42.
        Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:
    Input: s = "4193 with words"
    Output: 4193
    Explanation:
        Step 1: "4193 with words" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
                     ^
        The parsed integer is 4193.
        Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

Constraints:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

Notes:
    Instructions unclear... do we parse numbers with leading words, or...
    s = min(max(s, lower_bound), upper_bound): slower, but looks neat
    obvious tests, '', ' ', and float were lazily not included until failure
    percentile ranking wildly fluctuates with identical code ran seconds apart
"""


class Solution:
    # first attempt; 5 runtime errors provided useful test cases...
    def myAtoi(self, s: str) -> int:  # noqa
        # left whitespace strip
        s = s.lstrip(' ')

        # valid string check
        if not s:
            return 0

        # sign assignment
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # right strip non-digits
        if not s.isdigit():
            for i, each_char in enumerate(s):
                if not each_char.isdigit():
                    s = s[:i]
                    break

        # convert to signed int
        if s == '' or not s[0].isdigit():
            s = 0
        else:
            s = sign * int(float(s))

        # clamp boundaries
        lower_bound = -2 ** 31
        upper_bound = 2 ** 31 - 1
        if s < lower_bound:
            s = lower_bound
        elif s > upper_bound:
            s = upper_bound

        return s

    # second attempt: experimentation/optimization
    def second_attempt_myAtoi(self, s: str) -> int:  # noqa
        # left whitespace strip
        if s:
            for i, each_char in enumerate(s):
                if each_char != ' ':
                    s = s[i:]
                    break

        # valid string check
        if not s:
            return 0

        # sign assignment
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # right strip non-digits
        if not s.isdigit():  # isdigit() uses C standard library
            for i, each_char in enumerate(s):
                if not each_char.isdigit():
                    s = s[:i]
                    break

        # convert to signed int
        if s == '' or not s[0].isdigit():
            s = 0
        else:
            s = sign * int(float(s))

        # clamp boundaries
        lower_bound = -2 ** 31
        if s < lower_bound:
            s = lower_bound
        else:
            upper_bound = (-1 * lower_bound) - 1
            if s > upper_bound:
                s = upper_bound

        return s


class Test(Solution):
    tests = {
        # provided
        "42":
        42,
        "   -42":
        -42,
        "4193 with words":
        4193,

        # failed
        "words and 987":
        0,
        "3.14159":
        3,
        "":
        0,
        "00000-42a1234":
        0,
        " ":
        0,

    }

    def test_all(self):
        for each_test in self.tests.items():
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.myAtoi(test_input)
            try:
                assert actual_output == expected_output
                print("PASS", end="")
            except AssertionError:
                print("FAIL", end="")
            finally:
                print(f"  \t test_inp: {test_input}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")


Test().test_all()
