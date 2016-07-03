---
layout: leetcode
date: 2016-06-25
title: Swap Nodes in Pairs
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a linked list, swap every two adjacent nodes and return its head.
> For example,
> Given` 1->2->3->4`, you should return the list as `2->1->4->3`.
> Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
>     

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode Head;
    struct ListNode * before,* now,* after;
    Head.next = head;
    before = &Head;
    now = head;
    if( head == NULL)
        return head;
    after = head->next;
    while(after != NULL)
    {
        before->next = after;
        now->next = after->next;
        after->next = now;

        before = now;
        now = now->next;
        if(now == NULL)
            break;
        after = now->next;
    }
    return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
