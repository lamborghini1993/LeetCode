#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
using namespace std;

class Solution
{
  public:
    int uniquePaths(int m, int n)
    {
        int dp[110][110];
        int i, j;
        memset(dp, sizeof(dp), 0);
        for (i = 0; i < m; i++)
            dp[i][0] = 1;
        for (i = 0; i < n; i++)
            dp[0][i] = 1;
        for (i = 1; i < m; i++)
            for (j = 1; j < n; j++)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        return dp[m-1][n-1];
    }
};

int main(int argc, char const *argv[])
{
    printf("%d\n", Solution().uniquePaths(7, 3));
    return 0;
}
