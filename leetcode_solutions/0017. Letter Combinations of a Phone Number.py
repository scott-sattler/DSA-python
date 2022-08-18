"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.

Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:  # noqa
        pass


class Test(Solution):
    # format: (input, output)
    tests: list[
        tuple[
            str, list[str]
        ]
    ]

    tests = [
        # provided
        (
            "23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        ),
        (
            "", []
        ),
        (
            "2", ["a", "b", "c"]
        ),

        #
        (
            "", []
        ),

    ]

    def test_all(self, *include):
        pass_count = 0
        tests_failed = []
        for i, each_test in enumerate(self.tests):
            if len(include) > 0 and i not in include:
                continue
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.letterCombinations(test_input)
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

        tested = len(include) if len(include) > 0 else len(self.tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print(end='')


Test().test_all()
