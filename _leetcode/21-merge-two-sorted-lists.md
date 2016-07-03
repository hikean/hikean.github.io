---
layout: leetcode
date: 2016-06-25
title: Merge Two Sorted Lists
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
>
>

***

## Solution

**Result:** Accepted **Time:** 4ms

Here should be some explanations.

```c
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode head,*now;
    head.next = NULL;
    now=&head;
    while(l1 && l2)
    {
        if(l1->val < l2->val)
        {
            now -> next = l1;
            l1 = l1 -> next;
        }
        else
        {
            now -> next = l2;
            l2 = l2 -> next;
        }
        now = now -> next;
    }
    if(l2)
        l1 = l2;
    now -> next = l1;
    return head.next;
}

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
