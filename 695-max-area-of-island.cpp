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
    int row, col, dis[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}, result, tmp;
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        row = grid.size();
        if (row < 1)
            return 0;
        col = grid[0].size();
        // vector<bool> visc(col);
        vector<vector<bool>> vis(row, vector<bool>(col));
        result = 0;
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                vis[i][j] = false;
            }
        }

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (vis[i][j] || grid[i][j] == 0)
                    continue;
                vis[i][j] = true;
                tmp = 0;
                DFS(vis, grid, i, j);
                result = max(result, tmp);
            }
        }
        return result;
    }

    void DFS(vector<vector<bool>> &vis, vector<vector<int>> &grid, int i, int j)
    {
        tmp++;
        for (int t = 0; t < 4; t++)
        {
            int x = i + dis[t][0], y = j + dis[t][1];
            if (x < 0 || x >= row)
                continue;
            if (y < 0 || y >= col)
                continue;
            if (vis[x][y] || grid[x][y] == 0)
                continue;
            vis[x][y] = true;
            DFS(vis, grid, x, y);
        }
    }
};

int main()
{
    int h = 4, w = 5;
    int xh[h][w] = {{1, 1, 0, 0, 0},
                    {1, 1, 0, 0, 0},
                    {0, 0, 0, 1, 1},
                    {0, 0, 0, 1, 1}};
    vector<vector<int>> matrix; // 无初始化大小
    for (int i = 0; i < h; i++)
    {
        vector<int> tmp(xh[i], xh[i] + w);
        matrix.push_back(tmp);
    }
    printf("%d\n", Solution().maxAreaOfIsland(matrix));
    return 0;
}