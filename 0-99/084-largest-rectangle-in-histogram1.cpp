#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
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
        heights.push_back(0);
        stack<int> tmp;
        int t, result = 0, h, w;
        for (int i = 0; i <= n; i++)
        {

            if (tmp.empty() || heights[i] > heights[tmp.top()])
            {
                tmp.push(i);
                continue;
            }
            while (!tmp.empty() && heights[i] <= heights[tmp.top()])
            {
                h = tmp.top();
                tmp.pop();
                w = tmp.empty() ? i : i - tmp.top() - 1;
                result = max(result, heights[h] * w);
            }
            tmp.push(i);
        }
        return result;
    }
};

int main()
{
    int xh[] = {2, 1, 5, 6, 2, 3};
    vector<int> he(xh, xh + 6);
    printf("%d\n", Solution().largestRectangleArea(he));
    return 0;
}