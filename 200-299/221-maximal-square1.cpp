/*
 * @Description: 
 *  执行用时 : 68 ms, 在Maximal Square的C++提交中击败了6.93% 的用户
    内存消耗 : 11.3 MB, 在Maximal Square的C++提交中击败了0.52% 的用户
 * @Author: lamborghini1993
 * @Date: 2019-03-18 14:04:37
 * @UpdateDate: 2019-03-18 19:15:52
 */
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution
{
  public:
    int maximalSquare(vector<vector<char>> &matrix)
    {
        int h = matrix.size();
        if (h < 1)
            return 0;
        int w = matrix[0].size(), i, j, result = 0;
        vector<vector<int>> dp(h + 1, vector<int>(w + 1));

        // 防止重新计算第一行和第一列，dp数组往后移一位，dp初始化都为0
        // dp[i][j]：表示matrix[i-1][j-1]最大的正方形边长
        for (i = 1; i <= h; i++)
        {
            for (j = 1; j <= w; j++)
            {
                if (matrix[i - 1][j - 1] == '0')
                    continue;
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1;
                result = max(result, dp[i][j]);
            }
        }
        return result * result;
    }
};

int main()
{
    int h = 5, w = 8; // 16
    char xh[h][w] = {{'1', '1', '1', '1', '1', '1', '1', '1'},
                     {'1', '1', '1', '1', '1', '1', '1', '0'},
                     {'1', '1', '1', '1', '1', '1', '1', '0'},
                     {'1', '1', '1', '1', '1', '0', '0', '0'},
                     {'0', '1', '1', '1', '1', '0', '0', '0'}};

    // int h = 1, w = 1; // 1
    // char xh[h][w] = {{'1'}};

    vector<vector<char>> matrix;
    for (int i = 0; i < h; i++)
    {
        vector<char> tmp(xh[i], xh[i] + w);
        matrix.push_back(tmp);
    }
    int a = Solution().maximalSquare(matrix);
    printf("%d\n", a);
    return 0;
}