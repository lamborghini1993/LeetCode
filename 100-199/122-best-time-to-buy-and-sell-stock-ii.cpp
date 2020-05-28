/*
 * @Description: 5076 ms + 9.9 MB
 * @Author: lamborghini1993
 * @Date: 2019-03-15 16:53:50
 * @UpdateDate: 2019-03-15 17:03:04
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
    int dp[100000], cnt, result = 0;
    int maxProfit(vector<int> &prices)
    {
        cnt = prices.size();
        if (cnt < 2)
            return 0;
        dp[0] = 0;
        dp[1] = max(prices[1] - prices[0], 0);
        result = max(dp[1], result);
        for (int i = 2; i < cnt; i++)
        {
            int tmp = max(0, prices[i] - prices[0]);
            for (int j = 0; j < i; j++)
            {
                tmp = max(tmp, dp[j] + prices[i] - prices[j + 1]);
            }
            dp[i] = tmp;
            result = max(result, tmp);
        }
        return result;
    }
};