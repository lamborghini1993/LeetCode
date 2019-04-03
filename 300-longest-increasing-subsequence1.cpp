#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <set>
#include <climits>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution
{
  public:
    int lengthOfLIS(vector<int> &nums)
    {
        set<int> s;
        for (int num : nums)
        {
            set<int>::iterator it = s.lower_bound(num);
            if (it == s.end())
                s.insert(num);
            else
            {
                s.erase(it);
                s.insert(num);
            }
        }
        return s.size();
    }
};

int main()
{
    int N = 8;
    int xh[] = {10, 9, 2, 5, 3, 7, 101, 18};
    vector<int> t(xh, xh + N);
    printf("%d\n", Solution().lengthOfLIS(t));
    return 0;
}