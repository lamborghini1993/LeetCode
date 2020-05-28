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
    bool checkInclusion(string s1, string s2)
    {
        int l1 = s1.length(), l2 = s2.length();
        if (l1 > l2)
            return false;

        vector<int> xh(27); // xh[i] 表示差多少个达到标准
        int cnt = 0, t;     // cnt表示多少个不为0的
        for (auto c : s1)
        {
            t = c - 'a';
            xh[t]--;
            if (xh[t] == -1)
                cnt++;
        }

        for (int i = 0; i < l1; i++)
        {
            t = s2[i] - 'a';
            xh[t]++;
            if (xh[t] == 0)
                cnt--;
            if (xh[t] == 1)
                cnt++;
        }
        if (cnt == 0)
            return true;

        for (int i = l1; i < l2; i++)
        {

            if (s2[i] == s2[i - l1])
                continue;

            // 减去第i-l1个字符
            t = s2[i - l1] - 'a';
            xh[t]--;
            if (xh[t] == 0)
                cnt--;
            if (xh[t] == -1)
                cnt++;

            // 加上第i个字符
            t = s2[i] - 'a';
            xh[t]++;
            if (xh[t] == 0)
                cnt--;
            if (xh[t] == 1)
                cnt++;

            if (cnt == 0)
                return true;
        }
        return false;
    }
};

int main()
{
    string s1 = "aba", s2 = "bacbaa";
    printf("%d\n", Solution().checkInclusion(s1, s2));
    return 0;
}