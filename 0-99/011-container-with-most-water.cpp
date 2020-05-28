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
        for (int i = 0; i < height.size(); i++)
        {
            for (int j = i + 1; j < height.size(); j++)
            {
                tmp = (j - i) * min(height[i], height[j]);
                mx = max(mx, tmp);
            }
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
//     obj.maxArea(p);
//     return 0;
// }
