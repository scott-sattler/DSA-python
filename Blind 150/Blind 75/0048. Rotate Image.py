"""
90 cw
1 2  ->  3 1
3 4      4 2
transpose:
1 3
2 4
reflect about vertical center
3 1
4 2

90 ccw
1 3
2 4
reflect about horrizontal center
2 4
1 3

180
1 2
3 4
+90 cw
3 1
4 2
+90 cw
4 3
2 1

reflect about vertical center
2 1
4 3
reflect about horizontal center
4 3
2 1
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # transpose matrix
        def transpose(mat: List[List[int]]) -> None:
            n = len(mat)
            for i in range(n):
                for j in range(i + 1, n):
                    print(i, j)
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # reflect matrix about vertical center
        def reflect(mat: List[List[int]]) -> None:
            n = len(mat)
            for i in range(n):
                for j in range(n // 2):
                    mat[i][j], mat[i][(n - 1) - j] = mat[i][(n - 1) - j], mat[i][j]
                    # mat[i][ j], mat[i][-(j + 1)] = mat[i][-(j + 1)], mat[i][j]

        transpose(matrix)
        reflect(matrix)
        return matrix
