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
    int largestRectangleArea(vector<int> &heights)
    {
        int n = heights.size();
        if (n < 1)
            return 0;
        // 表示向左向右最多能延伸多远
        int *left = new int[n];
        int *right = new int[n];

        // 向右延伸
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--)
        {
            if (heights[i] > heights[i + 1])
            {
                right[i] = 1;
                continue;
            }
            int t = i + 1;
            while (t < n && heights[i] <= heights[t])
            {
                t += right[t];
            }
            right[i] = t - i;
        }

        // 向左延伸
        left[0] = 1;
        for (int i = 1; i < n; i++)
        {
            if (heights[i] > heights[i - 1])
            {
                left[i] = 1;
                continue;
            }
            int t = i - 1;
            while (t >= 0 && heights[i] <= heights[t])
            {
                t -= left[t];
            }
            left[i] = i - t;
        }
        int result = 0;
        for (int i = 0; i < n; i++)
        {
            result = max(result, (left[i] + right[i] - 1) * heights[i]);
        }
        return result;
    }
};