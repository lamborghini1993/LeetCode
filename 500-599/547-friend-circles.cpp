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
    int row, col;
    int findCircleNum(vector<vector<int>> &M)
    {
        row = M.size();
        if (row < 1)
            return 0;
        col = M[0].size();
        vector<bool> vis(row);
        int result = 0;
        for (int i = 0; i < row; i++)
        {
            if (vis[i])
                continue;
            vis[i] = true;
            DFS(vis, M, i);
            result++;
        }
        return result;
    }

    void DFS(vector<bool> &vis, vector<vector<int>> &grid, int x)
    {
        for (int i = 0; i < col; i++)
        {
            if (x == i || vis[i] || grid[x][i] == 0)
                continue;
            vis[i] = true;
            DFS(vis, grid, i);
        }
    }
};