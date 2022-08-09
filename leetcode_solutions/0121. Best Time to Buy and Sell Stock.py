"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""
import test_cases

# todo implement Kadane's Algorithm

class Solution:
    # second attempt: single-pass
    # time complexity: O(n)
    # space complexity: O(1)
    def maxProfit(self, prices: list[int]) -> int:  # noqa
        # always update new highest price
        # when encountering a new lowest
        #   record delta
        #   restart
        # greedy; dynamic programing

        low: int = 10 ** 4 + 1
        high: int = -1
        best_delta: int = 0

        for each_price in prices:
            if each_price > high:
                high = each_price

            if each_price < low:
                # record best thus far
                current_delta = high - low
                if current_delta > best_delta:
                    best_delta = current_delta

                # start new delta
                low = each_price
                high: int = -1
        else:
            current_delta = high - low
            if current_delta > best_delta:
                best_delta = current_delta

        return best_delta if best_delta > 0 else 0

    # first attempt: brute force double-loop
    # time complexity: O(n^2)
    def first_attempt_maxProfit(self, prices: list[int]) -> int:  # noqa
        # for each minimum value, look right for maximum

        low = 10 ** 4
        max_val = 0

        for i, each_price in enumerate(prices):
            if each_price < low:
                low = each_price
                high = low
                new_max = 0
                for j in range(i, len(prices)):
                    if prices[j] > high:
                        high = prices[j]
                        new_max = high - low
                else:
                    if new_max > max_val:
                        max_val = new_max

        return max_val


class Test(Solution):
    # format: ([input], output)
    tests = [
        # provided
        (
            [7, 1, 5, 3, 6, 4],
            5
        ),
        (
            [7, 6, 4, 3, 1],
            0
        ),

        #
        (
            [0],
            0
        ),
        (
            [5, 6, 4, 7, 3, 8, 2, 9],
            7
        ),
        (
            [1, 9],
            8
        ),
        (
            [11, 2, 9, 1],
            7
        ),

        # failed
        (
            test_cases.failed_test_1,
            3
        )

    ]

    def test_all(self,  *include):
        pass_count = 0
        tests_failed = []
        for i, each_test in enumerate(self.tests):
            if len(include) > 0 and i not in include:
                continue
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.maxProfit(test_input)
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
