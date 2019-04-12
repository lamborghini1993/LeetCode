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
    int trap(vector<int> &height)
    {
        int n = height.size();
        if (n <= 2)
            return 0;
        int result = 0;
        // left[i]表示左边最大柱子高度的下标
        int *left = new int[n];
        int *right = new int[n];
        int maxIndex = 0;
        for (int i = 1; i < n; i++)
        {
            if (height[i] > height[maxIndex])
            {
                maxIndex = i;
                left[i] = 0;
            }
            else
            {
                left[i] = maxIndex;
            }
        }
        maxIndex = n - 1;
        for (int i = n - 2; i > 0; i--)
        {
            if (height[i] > height[maxIndex])
            {
                right[i] = n - 1;
                maxIndex = i;
            }
            else
            {
                right[i] = maxIndex;
            }
        }

        for (int i = 1; i < n - 1; i++)
        {
            int hL = height[left[i]], hR = height[right[i]];
            if (hL > height[i] && hR > height[i])
            {
                result += (min(hL, hR) - height[i]);
            }
        }
        return result;
    }
};

int main()
{
    int xh[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    vector<int> he(xh, xh + 12);

    // int xh[] = {5, 4, 1, 2};
    // vector<int> he(xh, xh + 4);
    printf("%d\n", Solution().trap(he));
    return 0;
}