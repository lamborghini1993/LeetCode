#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
using namespace std;

class Solution
{
  public:
    int maxArea(vector<int> &height)
    {
        int mx = 0, tmp;
        int i = 0, j = height.size() - 1;
        while (i < j)
        {
            tmp = (j - i) * min(height[i], height[j]);
            mx = max(mx, tmp);
            if (height[i] > height[j])
                j--;
            else
                i++;
        }
        return mx;
    }
};

// int main(int argc, char const *argv[])
// {
//     vector<int> p;
//     int t[] = {1, 8, 6, 2, 5, 4, 8, 3, 7};
//     int iLen = sizeof(t) / sizeof(t[0]);
//     for (int i = 0; i < iLen; i++)
//         p.push_back(t[i]);
//     Solution obj = Solution();
//     printf("%d\n", obj.maxArea(p));
//     return 0;
// }
