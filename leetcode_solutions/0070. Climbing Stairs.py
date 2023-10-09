"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?


Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step


Constraints:
    1 <= n <= 45

"""


class Solution:  # noqa __init__ warning
    # bottom-up dp
    # tabulation
    # time: O(n)
    # space: O(n)
    def climbStairs(self, n: int) -> int:  # noqa naming
        if n < 2:
            return 1

        table = [0] * (n + 1)
        table[1] = 1
        table[2] = 2

        for i in range(3, n + 1):
            table[i] = table[i - 1] + table[i - 2]

        return table[-1]

    # top-down dp
    # memoization
    # time: O(n)
    # space: O(n) from O(1) input; O(n) memo; O(n) recursive call-stack
    def climbStairs(self, n: int) -> int:  # noqa naming
        memo = dict()
        return self._climbStairs(n, memo)

    def _climbStairs(self, n, memo):  # noqa naming
        if n < 2:
            return 1
        if n not in memo:
            memo[n] = self._climbStairs(n - 1, memo) + self._climbStairs(n - 2, memo)
        return memo[n]