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
    # first attempt: naive
    # time complexity: O(n+m) -> O(n)
    # space complexity:
    def getHint(self, secret: str, guess: str) -> str:  # noqa
        matches, out_of_order = 0, 0  # "bulls", "cows"
        guess_digits, secret_digits = {}, {}

        for i in range(len(guess)):  # note: len(guess) == len(secret)
            guess_digit = guess[i]
            secret_digit = secret[i]

            # check digits for match
            if guess_digit == secret_digit:
                matches += 1
                continue

            # add digits to hash
            if guess_digit in guess_digits:
                guess_digits[guess_digit] += 1
            else:
                guess_digits[guess_digit] = 1
            if secret_digit in secret_digits:
                secret_digits[secret_digit] += 1
            else:
                secret_digits[secret_digit] = 1

            # check digits for order: guess -?> secret
            if guess_digit in secret_digits:
                out_of_order += 1
                # update guess hash
                guess_digits[guess_digit] -= 1
                if guess_digits[guess_digit] == 0:
                    guess_digits.pop(guess_digit)
                # update secret hash
                secret_digits[guess_digit] -= 1
                if secret_digits[guess_digit] == 0:
                    secret_digits.pop(guess_digit)

            # check digits for order: secret -?> guess
            # compensates for multiple iterations
            if secret_digit in guess_digits:
                out_of_order += 1
                # update guess hash
                guess_digits[secret_digit] -= 1
                if guess_digits[secret_digit] == 0:
                    guess_digits.pop(secret_digit)
                # update secret hash
                secret_digits[secret_digit] -= 1
                if secret_digits[secret_digit] == 0:
                    secret_digits.pop(secret_digit)

        return f"{matches}A{out_of_order}B"


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
            "1807", "7810", "1A3B"
        ),
        (
            "1123", "0111", "1A1B"
        ),

        #
        (
            "111222", "222111", "0A6B"
        ),
        (
            "1", "2", "0A0B"
        ),
        (
            "1", "1", "1A0B"
        ),
        (
            "11", "11", "2A0B"
        ),
        (
            "111", "111", "3A0B"
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

                print(f"  \t test_{i:03d}: {each_test}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")

        tested = len(include) if len(include) > 0 else len(self.tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print(end='')


Test().test_all()
