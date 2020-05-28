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
    int tmp = INT_MAX, result = 0;
    int maxProfit(vector<int> &prices)
    {
        for (auto x : prices)
        {
            tmp = min(tmp, x);
            result = max(result, x - tmp);
        }
        return result;
    }
};