"""
733. Flood Fill
Easy

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the
pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.



Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels
    connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel is already colored 0, so no changes are made to the image.

Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 2^16
    0 <= sr < m
    0 <= sc < n
"""

import helper_functions as hf


class Solution:
    # fourth attempt: optimization
    # time complexity: O(V+E)?
    # space complexity: O(2V)?
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:  # noqa
        # graph traversal (dfs - stack)

        # stack/dfs pop a node
        #   when the pixel is the color to be filled
        #     get children (adjacent pixels to fill)
        #       add new children to open set
        #     fill pixel
        # add node to visited set

        start_px_color = image[sr][sc]
        visited = {}  # closed set; hash for lookup speed
        unvisited_list = {(sr, sc): ''}  # open set

        # while unexplored nodes exist
        while len(unvisited_list) > 0:
            # stack/dfs pop a node
            pixel = unvisited_list.popitem()[0]
            # when the pixel is the color to be filled
            if image[pixel[0]][pixel[1]] == start_px_color:
                # get children (adjacent pixels to fill)
                children = []

                north_child = (pixel[0] - 1, pixel[1])
                south_child = (pixel[0] + 1, pixel[1])
                east_child = (pixel[0], pixel[1] + 1)
                west_child = (pixel[0], pixel[1] - 1)

                if pixel[0] - 1 > -1:
                    children.append(north_child)
                if pixel[0] + 1 < len(image):
                    children.append(south_child)
                if pixel[1] + 1 < len(image[0]):
                    children.append(east_child)
                if pixel[1] - 1 > -1:
                    children.append(west_child)

                # add new children to open set
                for each_child in children:
                    if each_child not in visited:
                        if each_child not in unvisited_list:
                            unvisited_list[each_child] = ''
                # fill pixel
                image[pixel[0]][pixel[1]] = color
            # add node to visited set
            visited[pixel] = ''

        return image

    # third attempt: refactored to improve clarity
    # time complexity: O(V+E)?
    # space complexity: O(2V)?
    def third_attempt_floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:  # noqa
        # graph traversal (dfs - stack)

        # stack/dfs pop a node
        #   when the pixel is the color to be filled
        #     get children (adjacent pixels to fill)
        #       add new children to open set
        #     fill pixel
        # add node to visited set

        start_px_color = image[sr][sc]
        visited = {}  # closed set; hash for lookup speed
        unvisited_list = [(sr, sc)]  # open set

        # while unexplored nodes exist
        while len(unvisited_list) > 0:
            # stack/dfs pop a node
            pixel = unvisited_list.pop(-1)
            # when the pixel is the color to be filled
            if image[pixel[0]][pixel[1]] == start_px_color:
                # get children (adjacent pixels to fill)
                children = []

                north_child = (pixel[0] - 1, pixel[1])
                south_child = (pixel[0] + 1, pixel[1])
                east_child = (pixel[0], pixel[1] + 1)
                west_child = (pixel[0], pixel[1] - 1)

                if pixel[0] - 1 > -1:
                    children.append(north_child)
                if pixel[0] + 1 < len(image):
                    children.append(south_child)
                if pixel[1] + 1 < len(image[0]):
                    children.append(east_child)
                if pixel[1] - 1 > -1:
                    children.append(west_child)

                # add new children to open set
                for each_child in children:
                    if each_child not in visited:
                        if each_child not in unvisited_list:
                            unvisited_list.append(each_child)
                # fill pixel
                image[pixel[0]][pixel[1]] = color
            # add node to visited set
            visited.update({pixel: ''})

        return image

    # second attempt: refactored to improve clarity
    # time complexity: O(V+E)?
    # space complexity: O(2V)?
    def second_attempt_floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:  # noqa
        # graph traversal (dfs - stack)

        # stack/dfs pop a node
        #   when the pixel is the color to be filled
        #     get children (adjacent pixels to fill)
        #       add new children to open set
        #     fill pixel
        # add node to visited set

        start_px_color = image[sr][sc]
        visited = {}  # closed set; hash for lookup speed
        unvisited_list = [(sr, sc)]  # open set

        # while unexplored nodes exist
        while len(unvisited_list) > 0:
            # stack/dfs pop a node
            pixel = unvisited_list.pop(-1)
            # when the pixel is the color to be filled
            if image[pixel[0]][pixel[1]] == start_px_color:
                # get children (adjacent pixels to fill)
                img_size = (len(image), len(image[0]))
                found_children = self.get_children(pixel, img_size)
                # add new children to open set
                for each_child in found_children:
                    if each_child not in visited:
                        if each_child not in unvisited_list:
                            unvisited_list.append(each_child)
                # fill pixel
                image[pixel[0]][pixel[1]] = color
            # add node to visited set
            visited.update({pixel: ''})

        return image

    @staticmethod
    def get_children(pixel: tuple[int, int], img_size: tuple[int, int]) -> list[tuple[int, int]]:
        # order: cardinal directions (NSEW)
        children = []
        north_child = (pixel[0] - 1, pixel[1])
        south_child = (pixel[0] + 1, pixel[1])
        east_child = (pixel[0], pixel[1] + 1)
        west_child = (pixel[0], pixel[1] - 1)

        if pixel[0] - 1 > -1:
            children.append(north_child)
        if pixel[0] + 1 < img_size[0]:
            children.append(south_child)
        if pixel[1] + 1 < img_size[1]:
            children.append(east_child)
        if pixel[1] - 1 > -1:
            children.append(west_child)

        return children

    # first attempt: written for clarity and extensibility
    # obviously a failure
    # time complexity: O(V+E)?
    # space complexity: O(2V)?
    def first_attempt_floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:  # noqa
        # graph traversal (dfs - stack)

        # look cardinal directions
        # fill
        # track viewed nodes

        def get_children(element: tuple[int, int]) -> list[tuple[int, int]]:
            # order: cardinal directions (NSEW)
            children = []
            northern_child = (element[0] - 1, element[1])
            southern_child = (element[0] + 1, element[1])
            eastern_child = (element[0], element[1] + 1)
            western_child = (element[0], element[1] - 1)

            if bounds_check(northern_child):
                children.append(northern_child)
            if bounds_check(southern_child):
                children.append(southern_child)
            if bounds_check(eastern_child):
                children.append(eastern_child)
            if bounds_check(western_child):
                children.append(western_child)

            return children

        def bounds_check(element: tuple[int, int]) -> bool:
            # order: cardinal directions (NSEW)
            north = element[0] > -1
            south = element[0] < len(image)
            east = element[1] < len(image[0])
            west = element[1] > -1

            if north and south and east and west:
                return True
            return False

        start_px_color = image[sr][sc]
        visited = {}  # closed set; hash for lookup speed
        unvisited_list = [(sr, sc)]  # open set

        # while unexplored nodes exist
        while len(unvisited_list) > 0:
            # stack/dfs pop a node
            pixel = unvisited_list.pop(-1)
            # when the pixel is the color to be filled
            if image[pixel[0]][pixel[1]] == start_px_color:
                # get children (adjacent pixels to fill)
                found_children = get_children(pixel)
                # add new children to open set
                for each_child in found_children:
                    if each_child not in visited:
                        if each_child not in unvisited_list:
                            unvisited_list.append(each_child)
                # fill pixel
                image[pixel[0]][pixel[1]] = color
            # add node to visited set
            visited.update({pixel: ''})

        return image


class Test(Solution):
    """
    test format:
        input:      list[image, sr, sc, color]
        output:     filled image

    (sr, sc) is the starting fill position
    """

    tests: list[
        dict[
            str: [list[list[int]], int, int, int],
            str: list[list[int]]
        ]
    ]

    tests = [
        # provided
        {
            'input': [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2],
            'output': [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        },
        {
            'input': [[[0, 0, 0], [0, 0, 0]], 0, 0, 0],
            'output': [[0, 0, 0], [0, 0, 0]]
        },

        {
            'input': [[[0]], 0, 0, 0],
            'output': [[0]]
        },
        {
            'input': [[[1]], 0, 0, 0],
            'output': [[0]]
        },
        {
            'input': [[[1]], 0, 0, 2],
            'output': [[2]]
        },

        {
            'input': [[[1, 0], [0, 0]], 0, 0, 2],
            'output': [[2, 0], [0, 0]]
        },
        {
            'input': [[[0, 1], [0, 0]], 0, 1, 2],
            'output': [[0, 2], [0, 0]]
        },
        {
            'input': [[[0, 0], [1, 0]], 1, 0, 2],
            'output': [[0, 0], [2, 0]]
        },
        {
            'input': [[[0, 0], [0, 1]], 1, 1, 2],
            'output': [[0, 0], [0, 2]]
        },

        {
            'input': [[[2, 2], [2, 1]], 0, 0, 2],
            'output': [[2, 2], [2, 1]]
        },

        {
            'input': [[[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]], 0, 0, 0],
            'output': [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]
        },
        {
            'input': [[[0, 0, 0], [0, 0, 0]], 0, 0, 0],
            'output': [[0, 0, 0], [0, 0, 0]]
        },

    ]

    def test_all(self, *include, show_matrix: bool = False) -> None:
        pass_count = 0
        tests_failed = []
        for i, each_test in enumerate(self.tests):
            if len(include) > 0 and i not in include:
                continue
            input_matrix = each_test['input'][0]
            sr = each_test['input'][1]
            sc = each_test['input'][2]
            color = each_test['input'][3]

            matrix_copy = list(map(list, input_matrix))  # preserves input; floodFill modifies input
            output = self.floodFill(matrix_copy, sr, sc, color)
            expected_output = each_test['output']
            try:
                assert output == expected_output
                print("PASS", end="")
                pass_count += 1
            except AssertionError:
                print("FAIL", end="")
                tests_failed.append(i)
            finally:
                formatted_in = formatted_out = ''
                if show_matrix:
                    formatted_in = '\n' + hf.beautify_matrix(input_matrix, tab_offset=3) + '\n'*2
                    formatted_out = '\n' + hf.beautify_matrix(expected_output, tab_offset=3) + '\n'*2
                print(f"  \t test_{i:03d}: {str(each_test['input'])[1:-1]}\n"
                      f"{formatted_in}"
                      f"\t\t expd_out: {str(expected_output)}\n"
                      f"{formatted_out}"
                      f"\t\t test_out: {output}\n")

        tested = len(include) if len(include) > 0 else len(self.tests)
        print(f'SUMMARY: TESTED {tested} | PASSED {pass_count} | FAILED {len(tests_failed)}')
        print(f'FAILED TESTS: {[f"test_{i:03d}" for i in tests_failed]}') if len(tests_failed) > 0 else print(end='')


# Test().test_all(0, 1, 2, show_matrix=False)
# Test().test_all(0, 1, 2)
# Test().test_all(show_matrix=True)
Test().test_all()
