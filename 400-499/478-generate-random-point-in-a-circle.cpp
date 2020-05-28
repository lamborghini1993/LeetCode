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

const float PI = acos(-1);

class Solution
{
  public:
    double r, x, y;
    Solution(double radius, double x_center, double y_center)
    {
        r = radius;
        x = x_center;
        y = y_center;
    }
    double MyRand(double x)
    {
        int t = rand();
        double p = t * x / INT_MAX;
        return p;
    }

    vector<double> randPoint()
    {
        while (true)
        {
            float xx = MyRand(r) * 2 - r;
            float yy = MyRand(r) * 2 - r;
            printf("%f %f\n", xx, yy);
            if (xx * xx + yy * yy <= r * r)
            {
                return {xx + x, yy + y};
            }
        }
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj.randPoint();
 */

int main()
{
    double radius = 1;
    double x_center = 0;
    double y_center = 0;
    Solution obj = Solution(radius, x_center, y_center);
    for (int i = 0; i < 20; i++)
    {
        vector<double> result = obj.randPoint();
        printf("%f %f\n", result[0], result[1]);
    }
    return 0;
}