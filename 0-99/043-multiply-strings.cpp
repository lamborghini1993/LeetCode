#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
using namespace std;

class Solution
{
  public:
    int i, j, l1, l2, tmp;
    int result[222], n1[111], n2[111];

    string multiply(string num1, string num2)
    {
        l1 = num1.length();
        for (i = 0; i < l1; i++)
            n1[i] = num1[l1 - 1 - i] - '0';
        l2 = num2.length();
        for (i = 0; i < l2; i++)
            n2[i] = num2[l2 - 1 - i] - '0';
        Print(n1, l1);
        Print(n2, l2);
        memset(result, sizeof(result), 0);
        for (i = 0; i < l1; i++)
        {
            for (j = 0; j < l2; j++)
            {
                tmp = result[i + j] + n1[i] * n2[j];
                result[i + j] = tmp % 10;
                result[i + j + 1] += tmp / 10;
            }
        }
        Print(result, l1 + l2);
        string re = "";
        tmp = l1 + l2;
        while (tmp >= 1 && result[tmp] == 0)
        {
            tmp--; //排除末位0
        }
        for (i = tmp; i >= 0; i--)
        {
            re += result[i] + '0';
        }
        cout << re << endl;
        return re;
    }

    void Print(int t[], int size)
    {
        for (int i = 0; i < size; i++)
        {
            printf("%d", t[i]);
        }
        printf("\n");
    }
};

int main(int argc, char const *argv[])
{
    string s1 = "123", s2 = "456";
    Solution().multiply(s1, s2);
    return 0;
}
