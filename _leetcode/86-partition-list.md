---
layout: leetcode
date: 2016-06-28
title: Partition List
tags: [Linked List, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
>
>You should preserve the original relative order of the nodes in each of the two partitions.
>
>For example,
>
>Given `1->4->3->2->5->2` and x = `3`,
>
>return `1->2->2->4->3->5`.
>    

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
struct ListNode* partition(struct ListNode* head, int x) {
    struct ListNode low,up;
    struct ListNode *llast = &low, *ulast = & up,*tmp;
    while(head)
    {
        tmp = head;
        head = head ->next;
        if(tmp->val < x)
        {
            llast -> next = tmp;
            llast = tmp;
        }
        else
        {
            ulast -> next = tmp;
            ulast = tmp;
        }
    }
    ulast->next = NULL;
    llast->next = up.next;
    return low.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
