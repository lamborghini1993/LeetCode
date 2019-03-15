/*
 * @Description: 如果允许多次买入，求最大利益，其实就是：低买高卖，累积求利润和即可
 * @Author: lamborghini1993
 * @Date: 2019-03-15 16:53:50
 * @UpdateDate: 2019-03-15 17:05:41
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
    int maxProfit(vector<int> &prices)
    {
        int result = 0, tmp = INT_MAX;
        for (auto x : prices)
        {
            if (x < tmp)
            {
                tmp = x;
                continue;
            }
            result += (x - tmp);
            tmp = x;
        }
        return result;
    }
};