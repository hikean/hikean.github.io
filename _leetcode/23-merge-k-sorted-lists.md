---
layout: leetcode
date: 2016-06-26
title: Merge K Sorted Lists
tags: [Divide and Conquer, Linked List, Heap]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
>


***

## Solution

**Result:** Accepted **Time:** 48ms

Here should be some explanations.

```cpp
struct comp{
    bool operator()(const ListNode * lhs,const ListNode * rhs) const
    {
        return lhs->val > rhs->val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode head(0),*now,*tmp;
        head.next = NULL;
        now = &head;

        priority_queue<ListNode *,vector<ListNode*>,comp> que;
        for(auto i = lists.begin(); i != lists.end(); ++i)
        {
            if((*i))
                que.push(*i);
        }
        while(!que.empty())
        {
            tmp = que.top();que.pop();
            now -> next = tmp;
            now = now -> next;
            if(tmp->next)
                que.push(tmp->next);
        }
        now -> next = NULL;
        return head.next;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n*k*log(k))$$
- Space Complexity: $$O(1)$$
