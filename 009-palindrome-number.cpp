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
    bool isPalindrome(int x)
    {
        vector<int> t;
        if (x < 0)
            return false;
        if (x < 10)
            return true;
        while (x)
        {
            t.push_back(x % 10);
            x /= 10;
        }
        for (int i = 0; i < t.size() / 2; i++)
        {
            if (t[i] != t[t.size() - i - 1])
                return false;
        }
        return true;
    }
};