"""
278. First Bad Version
Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the
first bad version. You should minimize the number of calls to the API.

Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
        call isBadVersion(3) -> false
        call isBadVersion(5) -> true
        call isBadVersion(4) -> true
        Then 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1

Constraints:
    1 <= bad <= n <= 2^31 - 1
"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:  # noqa
    """ defined in testing """
    pass


class Solution:
    # first attempt
    # time complexity: O(log n)
    # space complexity: O(1)
    def firstBadVersion(self, n: int) -> int:  # noqa
        # binary search to find the leftmost 'bad' element
        left_index = 0
        right_index = n + 1

        while True:
            n = left_index + ((right_index - left_index) // 2)
            if isBadVersion(n):  # true, look left
                right_index = n
                if not isBadVersion(n - 1):
                    return n
            else:  # false, look right
                left_index = n
                if isBadVersion(n + 1):
                    return n + 1


class Test(Solution):
    # format: ((n, bad), output)
    tests = [
        # provided
        (
            (5, 4),
            4
        ),
        (
            (1, 1),
            1
        ),

        (
            (11, 3),
            3
        ),
        (
            (11, 2),
            2
        ),
        (
            (11, 1),
            1
        ),
        (
            (12, 3),
            3
        ),
        (
            (12, 2),
            2
        ),
        (
            (12, 1),
            1
        ),
        (
            (1, 1),
            1
        ),
        (
            (2, 1),
            1
        ),
        (
            (3, 1),
            1
        ),
        (
            (2, 2),
            2
        ),
        (
            (3, 3),
            3
        ),
        (
            (4, 4),
            4
        ),

    ]

    def test_all(self):
        pass_count = 0
        for each_test in self.tests:
            test_input = each_test[0][0]
            expected_output = each_test[1]
            globals()['isBadVersion'] = lambda x: True if x >= expected_output else False  # re/define isBadVersion
            actual_output = self.firstBadVersion(test_input)
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
