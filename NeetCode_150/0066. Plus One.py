"""
[9, 9, 9]

O(n)
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  # noqa
        digits[-1] += 1

        remainder = 0
        for i in range(-1, -len(digits) - 1, -1):
            curr_digit = digits[i] + remainder
            digits[i] = curr_digit % 10
            remainder = curr_digit // 10

        if remainder > 0:
            digits.insert(0, 1)

        return digits
