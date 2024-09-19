from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return 0
        result = 0
        dp = [[0] * col for _ in range(row)]  # 第i行，从左到右，最大连续1的数量
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "0":
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                result = max(result, dp[i][j])
        return result**2

    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     lx_row = [[0] * col for _ in range(row)]  # 第i行，从左到右，最大连续1的数量
    #     lx_col = [[0] * col for _ in range(row)]  # 第j列，从上到下，最大连续1的数量
    #     dp = [[0] * col for _ in range(row)]

    #     for k in range(row):
    #         dp[k][0] = lx_row[k][0] = 1 if matrix[k][0] == "1" else 0
    #     for k in range(row):
    #         dp[0][k] = lx_col[0][k] = 1 if matrix[0][k] == "1" else 0

    #     for i in range(1, row):
    #         for j in range(1, col):
    #             add_num = 1 if matrix[i][j] == "1" else 0
    #             lx_row[i][j] = lx_row[i][j - 1] + add_num
    #             lx_col[i][j] = lx_col[i - 1][j] + add_num

    #     for i in range(1, row):
    #         for j in range(1, col):
    #             if matrix[i][j] == "0":
    #                 continue
    #             dp[i][j] = 1
    #             edge = dp[i - 1][j - 1]
    #             if lx_row[i][j] >= edge + 1 and lx_col[i][j] >= edge + 1:
    #                 dp[i][j] = edge + 1

    #     result = 0
    #     for i in range(row):
    #         for j in range(col):
    #             result = max(result, dp[i][j])

    #     return result**2


func = Solution().maximalSquare
print(func([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(func([["0", "1"]]))
