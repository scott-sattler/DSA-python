"""
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.


Example 1:
    Input: grid = [
      ['1','1','1','1','0'],
      ['1','1','0','1','0'],
      ['1','1','0','0','0'],
      ['0','0','0','0','0']
    ]
    Output: 1

Example 2:
    Input: grid = [
      ['1','1','0','0','0'],
      ['1','1','0','0','0'],
      ['0','0','1','0','0'],
      ['0','0','0','1','1']
    ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:  # noqa
        pass


class Test(Solution):
    tests: list[
        tuple
        [
            list[list[str]],
            int
        ]
    ]
    tests = list()

    example_test_1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    example_test_1_output = 1
    tests.append((example_test_1, example_test_1_output))

    example_test_2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    example_test_2_output = 3
    tests.append((example_test_2, example_test_2_output))

    def test_all(self):
        for each_test in self.tests:
            output = self.numIslands(each_test[0])
            expected_output = each_test[1]
            try:
                assert output == expected_output
                print("PASS", end="")
            except AssertionError:
                print("FAIL", end="")
            finally:
                formatted_out = '\n\t\t ' + str(each_test[0]).replace('],', '],\n' + '\t\t')[1:-1] + '\n'
                print(f"  \t test_inp: {each_test[0]}\n"
                      f"{formatted_out}\n"
                      f"\t\t expd_out: {expected_output}\n"
                      f"\t\t test_out: {output}\n")


Test().test_all()
