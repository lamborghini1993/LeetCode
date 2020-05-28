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
    int lengthOfLongestSubstring(string s)
    {
        int t, result = 0, index = 0, lastSameIndex = 0;
        vector<int> p(200);
        for (auto c : s)
        {
            index++;
            t = c;
            if (p[t])
                lastSameIndex = max(lastSameIndex, p[t]);
            p[t] = index;   // 这里index如果为0的话，荣易判断失误，所以从1开始
            result = max(result, index - lastSameIndex);
        }
        return result;
    }
};

int main()
{
    string s = "abcabcbb";
    printf("%d\n", Solution().lengthOfLongestSubstring(s));
    return 0;
}