"""
55. Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5

"""


class Solution:
    # first attempt
    # time complexity: O(n)
    # space complexity: O(1)
    def canJump(self, nums: list[int]) -> bool:  # noqa: naming convention
        # left to right
        # track max distance from current point
        # greedy
        n = len(nums)
        max_distance = 0
        for i in range(n - 1):
            # max distance
            max_distance = max(max_distance, nums[i])

            # fails if max ever falls below 1
            if max_distance < 1:
                return False
            max_distance -= 1

        return True


# taken from 0299; modified
class Test:
    # format: [ ( input , expected_out ), ]
    test_cases: list[tuple[list, bool]] = [
        # provided
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),

        # additional
        ([5, 0, 0, 0, 0], True),
        ([3, 0, 0, 0, 0], False),
        ([4, 0, 0, 0, 0], True),

        ([0], True),
        ([1], True),

        ([0, 5, 5, 5, 5], False),
        ([99, 0, 0, 0, 0], True),

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
            actual_output = s.canJump(test_input)
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
