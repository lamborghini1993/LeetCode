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

ListNode *AddListNode(int t[], int size)
{
    ListNode *head = NULL, *first = NULL, *current = NULL;
    if (size == 0)
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
    int i, t, lsize;

    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if (lists.size() == 0)
            return NULL;
        lsize = lists.size();
        // 归并合并
        while (lsize > 1)
        {
            t = (1 + lsize) / 2;
            for (i = 0; i < lsize / 2; i++)
            {
                lists[i] = mergeTwoLists(lists[i], lists[i + t]);
                // printf("mergeTwoLists %d:", i);
                // nodeprint(lists[i]);
            }
            lsize = t;
        }
        return lists[0];
    }

    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode *head, *cur;
        head = cur = new ListNode(0);
        // nodeprint(l1);
        // nodeprint(l2);
        while (l1 && l2)
        {
            if (l1->val > l2->val)
            {
                cur->next = l2;
                l2 = l2->next;
            }
            else
            {
                cur->next = l1;
                l1 = l1->next;
            }
            cur = cur->next;
        }
        if (l1)
            cur->next = l1;
        if (l2)
            cur->next = l2;
        // nodeprint(head->next);
        return head->next;
    }

    void nodeprint(ListNode *print)
    {
        while (print)
        {
            cout << print->val << " ";
            print = print->next;
        }
        cout << endl;
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
