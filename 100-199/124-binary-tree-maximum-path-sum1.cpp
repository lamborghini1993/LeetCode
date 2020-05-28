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

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
  public:
    int result = INT_MIN;
    int maxPathSum(TreeNode *root)
    {
        DFS(root);
        return result;
    }

    int DFS(TreeNode *temp)
    {
        if (temp == NULL)
            return 0;
        int left, right;
        left = max(0, DFS(temp->left));
        right = max(0, DFS(temp->right));
        result = max(result, temp->val + left + right);
        return max(temp->val, temp->val + max(left, right));
    }
};