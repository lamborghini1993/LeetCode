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

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
vector<ListNode *> mylists;
int i;

ListNode *AddListNode(int t[], int size)
{
    ListNode *head = NULL, *first = NULL, *current = NULL;
    if(size==0)
        return head;
    head = first = new ListNode(t[0]);
    for (int i = 1; i < size; i++)
    {
        current = new ListNode(t[i]);
        first->next = current;
        first = first->next;
    }
    mylists.push_back(head);
    return head;
}

class Solution
{
  public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        ListNode *result = NULL;
        if(lists.size() == 0)
            return result;
        int t[999999], cnt = 0;
        for (i = 0; i < lists.size(); i++)
        {
            while (lists[i])
            {
                t[cnt++] = lists[i]->val;
                lists[i] = lists[i]->next;
            }
        }
        sort(t, t + cnt);
        for (i = 0; i < cnt; i++)
            cout << t[i] << " ";
        cout << endl;
        ListNode *head = AddListNode(t, cnt);
        result = head;
        while (head)
        {
            cout << head->val << "->";
            head = head->next;
        }
        cout << endl;
        return result;
    }
};

int main(int argc, char const *argv[])
{
    int t1[] = {1, 4, 5};
    int t2[] = {1, 3, 4};
    int t3[] = {2, 6};
    AddListNode(t1, 3);
    AddListNode(t2, 3);
    AddListNode(t3, 2);
    ListNode *result = Solution().mergeKLists(mylists);
    return 0;
}
