/*
 * @Description: 
 *  执行用时 : 108 ms, 在Maximal Square的C++提交中击败了2.45% 的用户
    内存消耗 : 14.4 MB, 在Maximal Square的C++提交中击败了0.52% 的用户
 * @Author: lamborghini1993
 * @Date: 2019-03-18 14:04:37
 * @UpdateDate: 2019-03-18 14:05:21
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

const int N = 500;

class Solution
{
  public:
    int dp[N][N], row[N][N], col[N][N];
    int maximalSquare(vector<vector<char>> &matrix)
    {
        int h = matrix.size();
        if (h < 1)
            return 0;
        int w = matrix[0].size(), t, i, j, result = 0, cnt;

        for (i = 0; i < h; i++)
        {
            cnt = 0;
            for (j = 0; j < w; j++)
            {
                t = dp[i][j] = matrix[i][j] - '0';
                if (t)
                    cnt++;
                else
                    cnt = 0;
                row[i][j] = cnt;
            }
        }

        for (j = 0; j < w; j++)
        {
            cnt = 0;
            for (i = 0; i < h; i++)
            {
                if (dp[i][j])
                    cnt++;
                else
                    cnt = 0;
                col[i][j] = cnt;
            }
        }

        for (i = 0; i < h; i++)
        {
            result = max(result, dp[i][0]);
        }
        for (j = 0; j < w; j++)
        {
            result = max(result, dp[0][j]);
        }

        for (i = 1; i < h; i++)
        {
            for (j = 1; j < w; j++)
            {
                if (!dp[i][j])
                    continue;
                t = min(dp[i - 1][j - 1], min(col[i - 1][j], row[i][j - 1]));
                dp[i][j] = t + 1;
                result = max(result, dp[i][j]);
            }
        }
        return result * result;
    }
};

int main()
{
    int h = 5, w = 8;
    char xh[h][w] = {{'1', '1', '1', '1', '1', '1', '1', '1'},
                     {'1', '1', '1', '1', '1', '1', '1', '0'},
                     {'1', '1', '1', '1', '1', '1', '1', '0'},
                     {'1', '1', '1', '1', '1', '0', '0', '0'},
                     {'0', '1', '1', '1', '1', '0', '0', '0'}};

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