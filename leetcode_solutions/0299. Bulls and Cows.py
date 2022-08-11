"""
299. Bulls and Cows
Medium

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you
provide a hint with the following info:

    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong
    position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both
secret and guess may contain duplicate digits.

Example 1:
    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1807"
      |
    "7810"

Example 2:
    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1123"        "1123"
      |      or     |
    "0111"        "0111"
    Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to
    allow one 1 to be a bull.

Constraints:
    1 <= secret.length, guess.length <= 1000
    secret.length == guess.length
    secret and guess consist of digits only.
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:  # noqa
        pass


class Test(Solution):
    # format: (input: secret, input: guess, output)
    tests: list[
        tuple[
            str, str, str
        ]
    ]

    tests = [
        # provided
        (
            "1807", "7810", "1A1B"
        ),
        (
            "1123", "0111", "1A1B"
        ),

        #
        (
            "", "", ""
        ),

    ]

    def test_all(self, *include):
        pass_count = 0
        tests_failed = []
        for i, each_test in enumerate(self.tests):
            if len(include) > 0 and i not in include:
                continue
            test_input = each_test[:-1]
            expected_output = each_test[2]
            actual_output = self.getHint(test_input[0], test_input[1])
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
                tests_failed.append(i)
            finally:

                print(f"  \t test_{i:03d}: {each_test[0]}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")

        tested = len(include) if len(include) > 0 else len(self.tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print(end='')


Test().test_all()
