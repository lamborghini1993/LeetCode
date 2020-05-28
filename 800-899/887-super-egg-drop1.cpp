/*
 * @Description: 
 * 执行用时: 16 ms, 在Super Egg Drop的C++提交中击败了40.18% 的用户
 * 内存消耗: 9.2 MB, 在Super Egg Drop的C++提交中击败了41.67% 的用户
 * @Author: lamborghini1993
 * @Date: 2019-02-25 21:24:00
 * @UpdateDate: 2019-02-25 21:32:09
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
using namespace std;

const int T = 10001;

int xh[101][T]; // xh[i][j]表示：i个鸡蛋扔j次最多能测试多少层楼
int i, j;

class Solution
{
  public:
    int superEggDrop(int K, int N)
    {
        for (i = 1; i <= K; i++)
        {
            xh[i][1] = 1;
        }
        for (i = 1; i < T; i++)
        {
            xh[1][i] = i;
        }
        for (i = 2; i <= K; i++)
        {
            for (j = 2; j < T; j++)
            {
                if (i >= j)
                    xh[i][j] = xh[j][j];
                xh[i][j] = xh[i - 1][j - 1] + 1 + xh[i][j - 1];
                // printf("xh[%d][%d]=%d\n", i, j, xh[i][j]);
                if (xh[i][j] >= 10000)
                    break;
            }
        }

        for (i = 1; i < T; i++)
        {
            // printf("xh[%d][%d]=%d\n", K, i, xh[K][i]);
            if (xh[K][i] >= N)
                return i;
        }
        return 0;
    }
};

int main()
{
    printf("%d\n", Solution().superEggDrop(3, 14));
}