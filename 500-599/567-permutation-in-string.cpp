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
        sort(s1.begin(), s1.end());
        for (int i = 0; i < l2 - l1 + 1; i++)
        {
            string tmp = s2.substr(i, l1);
            sort(tmp.begin(), tmp.end());
            if (s1 == tmp)
                return true;
        }
        return false;
    }
};