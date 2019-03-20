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
    string GetSubStr(string s, int index)
    {
        if (index <= 0)
            return "";
        string rr(s, 0, index);
        return rr;
    }
    string longestCommonPrefix(vector<string> &strs)
    {
        int size = strs.size(), i, index = 0;
        if (size <= 0)
            return "";
        char c;
        while (true)
        {
            if (strs[0].length() <= index)
            {
                return GetSubStr(strs[0], index);
            }
            c = strs[0][index];
            for (i = 1; i < size; i++)
            {
                if (strs[i].length() <= index || strs[i][index] != c)
                {
                    return GetSubStr(strs[i], index);
                }
            }
            index++;
        }
    }
};