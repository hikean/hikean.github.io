---
layout: leetcode
date: 2016-07-13
title: Linked List Cycle
tags: [Linked List, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a linked list, determine if it has a cycle in it.
>
>**Follow up:**
>
>Can you solve it without using extra space?
>
>     

***

## Solution

**Result:** Accepted **Time:** 7 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode * p1 = head, *p2 = head;
    while(p2)
    {
        p2 = p2->next;
        if(p2 == p1) return true;
        if(p2 == NULL) return false;
        p2 = p2->next;
        if(p2 == p1) return true;
        p1 = p1->next;
    }
    return false;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
