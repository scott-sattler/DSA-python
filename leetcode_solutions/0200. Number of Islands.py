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

import test_cases


class Solution:
    # first attempt
    def numIslands(self, grid: list[list[str]]) -> int:  # noqa
        # island defined as land surrounded by water
        #   1 with 0s NSEW
        # DFS grid traversal

        count = 0
        explored_nodes = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                seed_node = (i, j)
                if grid[seed_node[0]][seed_node[1]] == '0':
                    explored_nodes.append(seed_node)
                    continue
                if seed_node not in explored_nodes:
                    found_nodes = [seed_node]  # seed
                    island_nodes = []

                    while found_nodes:
                        inspected_node = found_nodes.pop(-1)
                        if grid[inspected_node[0]][inspected_node[1]] == '1':
                            island_nodes.append(inspected_node)

                            new_nodes = self.find_nodes(grid, inspected_node)
                            # found_nodes += [each_node for each_node in new_nodes if each_node not in explored_nodes]
                            for each_node in new_nodes:
                                if each_node not in explored_nodes:
                                    found_nodes.append(each_node)

                        explored_nodes.append(inspected_node)

                    if len(island_nodes) > 0:
                        count += 1
                        print(count)

        return count

    # find boundary-checked nodes
    @staticmethod
    def find_nodes(grid: list[list], element: tuple[int, int], ) -> list[tuple[int, int]]:
        discovered_nodes = []
        # cardinal directions: NSEW
        north_node = (element[0] - 1, element[1])
        if north_node[0] >= 0:
            discovered_nodes.append(north_node)
        south_node = (element[0] + 1, element[1])
        if south_node[0] < len(grid):
            discovered_nodes.append(south_node)
        east_node = (element[0], element[1] + 1)
        if east_node[1] < len(grid[0]):
            discovered_nodes.append(east_node)
        west_node = (element[0], element[1] - 1)
        if west_node[1] >= 0:
            discovered_nodes.append(west_node)

        return discovered_nodes


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

    tests.append((test_cases.failed_test_0, 0))

    def test_all(self, include: list[int] | None = None):
        for each_test in self.tests:
            if include is not None and self.tests.index(each_test) not in include:
                continue
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


Test().test_all(include=[2])

# foo = Test().discover_nodes(Test().tests[0][0], (1, 1))
# print(foo)
