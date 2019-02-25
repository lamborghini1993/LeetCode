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

int xh[101][10001];
int i, j, o, temp, result;

class Solution  //超时
{
  public:
    int superEggDrop(int K, int N)
    {
        for (i = 1; i <= K; i++)
        {
            xh[i][1] = 1;
            xh[i][0] = 0;
        }
        for (i = 1; i <= N; i++)
        {
            xh[1][i] = i;
        }
        for (i = 2; i <= K; i++)
        {
            for (j = 2; j <= N; j++)
            {
                result = 0x7fffffff;
                for (o = 2; o <= j; o++)
                {
                    temp = max(xh[i - 1][o - 1], xh[i][j - o]);
                    // printf("xh[%d][%d]=%d ", i - 1, o - 1, xh[i - 1][o - 1]);
                    // printf("xh[%d][%d]=%d ", i - 1, N - o, xh[i][j - o]);
                    // printf("max=%d\n", temp);
                    result = min(result, temp);
                }
                xh[i][j] = 1 + result;
                // printf("xh[%d][%d]=%d\n", i, j, xh[i][j]);
            }
        }
        return xh[K][N];
    }
};

int main()
{
    printf("%d\n", Solution().superEggDrop(6, 10000));
}