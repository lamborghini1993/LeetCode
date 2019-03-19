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
    int maxEnvelopes(vector<pair<int, int>> &envelopes)
    {
        int size = envelopes.size();
        if (size == 0)
            return 0;
        if (size == 1)
            return 1;

        vector<int> enp;
        // 对envelopes先按照第一个元素从小到大排序，然后按照第二个元素从大到小排序
        sort(envelopes.begin(), envelopes.end(), [](const pair<int, int> &a, const pair<int, int> &b) {
            if (a.first == b.first)
                return a.second > b.second;
            return a.first < b.first;
        });
        // for (auto x : envelopes)
        //     printf("%d %d\n", x.first, x.second);
        for (int i = 0; i < size; ++i)
        {
            auto it = lower_bound(enp.begin(), enp.end(), envelopes[i].second);
            // 函数lower_bound()在first和last中的前闭后开区间进行二分查找，返回大于或等于val的第一个元素位置。如果所有元素都小于val，则返回last的位置
            // 函数upper_bound()在first和last中的前闭后开区间进行二分查找，返回大于val的第一个元素位置。如果所有元素都小于val，则返回last的位置
            if (it == enp.end())
                enp.push_back(envelopes[i].second);
            else
                *it = envelopes[i].second;
        }
        return enp.size();
    }
};

int main()
{
    vector<pair<int, int>> vec;
    vec.push_back(make_pair(2, 3));
    vec.push_back(make_pair(5, 4));
    vec.push_back(make_pair(6, 7));
    vec.push_back(make_pair(6, 5));
    vec.push_back(make_pair(7, 6));
    Solution().maxEnvelopes(vec);
    return 0;
}