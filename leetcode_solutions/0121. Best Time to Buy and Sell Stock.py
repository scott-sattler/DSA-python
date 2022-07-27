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


class Solution:
    # first attempt
    def maxProfit(self, prices: list[int]) -> int:  # noqa
        pass


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

    ]

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.maxProfit(test_input)
            try:
                assert actual_output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
            finally:

                print(f"  \t test_inp: {each_test[0]}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {actual_output}\n")
        print(f'SUMMARY: TESTED {len(self.tests)} | PASSED {pass_count} | FAILED {len(self.tests) - pass_count}')


Test().test_all()
