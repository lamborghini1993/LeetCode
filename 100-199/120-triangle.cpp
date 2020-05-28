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
    int minimumTotal(vector<vector<int>> &triangle)
    {
        for (int i = triangle.size() - 2; i >= 0; i--)
        {
            for (int j = 0; j < triangle[i].size(); j++)
            {
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        return triangle[0][0];
    }
};

int main()
{
    int n = 4;
    int xh[n][n] = {{2},
                    {3, 4},
                    {6, 5, 7},
                    {4, 1, 8, 3}};
    vector<vector<int>> triangle;
    for (int i = 0; i < n; i++)
    {
        vector<int> tmp(xh[i], xh[i] + i + 1);
        triangle.push_back(tmp);
    }
    printf("%d\n", triangle[0][0]);
    int result = Solution().minimumTotal(triangle);
    printf("%d\n", result);
    return 0;
}