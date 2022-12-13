"""
402. Remove K Digits
Medium

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after
removing k digits from num.

Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.

Notes:
    While the problem statement does not specify the following condition, the objective is to remove the three largest
    /consecutive/ digits (or "smallest possible integer after removing k [consecutive] digits from num").

    Also not included in the description: you /must/ remove k digits...

    Made somewhat clear via Example 2, "Note that the output must not contain leading zeroes.", is actually: solutions
    that contain a leading zero are not valid.
"""


class Solution:
    # first attempt

    def removeKdigits(self, num: str, k: int) -> str:  # noqa: naming convention

        return ''


# taken from 0055
class Test:
    # format: [ ( input , expected_out ), ]
    test_cases: list[tuple[list, bool]] = [
        # provided
        (("1432219", 3), "1219"),
        (("10200", 1), "100"),
        (("10", 2), "0"),

        # additional
        (("0", 0), "0"),
        (("0", 1), "0"),
        (("0", 99), "0"),
        (("0000", 0), "0"),
        (("0000", 1), "0"),
        (("0000", 99), "0"),

        # leading zeros
        (("0321", 3), "0"),
        (("0000321", 3), "0"),
        (("0000321", 1), "21"),
        (("0000321", 2), "1"),
        # trailing zeros
        (("973000", 3), "0"),
        (("647", 1), "64000"),
        (("642000", 2), "2000"),

    ]

    def test_all(self, *include):
        """
        :param include: eg .test_all(0, 2, 5); or .test_all()
        :return: None
        """
        tests = self.test_cases
        s = Solution()

        pass_count = 0
        tests_failed = []
        for i, each_test in enumerate(tests):
            if len(include) > 0 and i not in include:
                continue
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = s.removeKdigits(test_input[0], test_input[1])  # <--- fn name here
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
                tests_failed.append(i)
            finally:

                print(f"  \t test_{i:03d}: {each_test}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")

        tested = len(include) if len(include) > 0 else len(tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print(end='')


# example usages
# Test().test_all(0, 2, 5); Test().test_all()
Test().test_all()
