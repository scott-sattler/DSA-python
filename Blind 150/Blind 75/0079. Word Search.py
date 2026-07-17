"""
can we find a defined path (where multiple paths can exist)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # noqa
        visited = set()

        def dfs(i, j, w_index):
            # valid progression check
            if w_index == len(word):
                return True

            # bounds checks
            if i < 0 or j < 0:
                return False
            if i >= ROWS or j >= COLS:
                return False

            if board[i][j] != word[w_index]:
                return False

            # check for, and mark as, visited
            if (i, j) in visited:
                return False
            visited.add((i, j))

            # explore
            result = (
                       dfs(i + 1, j, w_index + 1)
                    or dfs(i - 1, j, w_index + 1)
                    or dfs(i, j + 1, w_index + 1)
                    or dfs(i, j - 1, w_index + 1)
            )

            # backtrack
            visited.remove((i, j))

            return result

        for row in range(ROWS):
            for col in range(COLS):
                visited = set()
                if dfs(row, col, w_index=0):
                    return True
        return False