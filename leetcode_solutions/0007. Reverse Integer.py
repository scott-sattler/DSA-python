"""
7. Reverse Integer
Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = 120
    Output: 21

Constraints:
    -2^31 <= x <= 2^31 - 1
"""


class Solution:
    # second attempt: referenced mostly useless approaches
    # poor approach to solution (using strings); not optimized
    def reverse(self, x: int) -> int:  # noqa
        # if same order of magnitude (10)
        # read right to left
        #   compare to boundary value
        #     if greater, return 0
        #     if equal, continue
        #     if less, return number

        reversed_signed_int = str(abs(x))[::-1]
        max_val = 2 ** 31 - 1
        oom = len(str(max_val))  # order of magnitude
        if len(reversed_signed_int) < oom:
            return int(reversed_signed_int) if x > 0 else -int(reversed_signed_int)
        elif len(reversed_signed_int) == oom:
            for i, each_digit in enumerate(reversed_signed_int):
                if i == len(reversed_signed_int) or each_digit < str(max_val)[i]:
                    return int(reversed_signed_int) if x > 0 else -int(reversed_signed_int)
                # can ignore +- differences due to input constraint
                if each_digit == str(max_val)[i]:
                    continue
                if each_digit > str(max_val)[i]:
                    break
        return 0

    # solve for correctness
    # incorrect solution: environment disallows 64-bit int storage
    def first_attempt_reverse(self, x: int) -> int:  # noqa
        sign = 1
        if x < 1:
            sign = -1

        # casting int removes leading zeroes
        reversed_signed_int = int(str(x).strip('-')[::-1])

        if -2 ** 31 <= reversed_signed_int < 2 ** 31:
            return sign * reversed_signed_int
        else:
            return 0


class Test(Solution):
    tests = {
        123:
            321,
        -123:
            -321,
        120:
            21,
        # edge cases:
        2_147_483_648:  # 2^31 - 1 + 1; 2,147,483,648
            0,
        -2_147_483_649:  # -2^31 - 1; -2,147,483,649
            0,
        # x is said to be constrained to exclude interesting edge cases... ?
        9_463_841_472:
            0,

        2_147_447_412:  # largest number without overflow
            2_147_447_412,

        1_534_236_469:
            0,

    }

    def test_all(self):
        for each_test in self.tests.items():
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.reverse(test_input)
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

