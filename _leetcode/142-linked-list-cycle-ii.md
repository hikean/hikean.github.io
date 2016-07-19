---
layout: leetcode
date: 2016-07-13
title: Linked List Cycle II
tags: [Linked List, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
>
>**Note:** Do not modify the linked list.
>
>**Follow up:**
>
>Can you solve it without using extra space?
>
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode * fast = head, *slow = head;
    do
    {
        if(fast == NULL || fast->next == NULL)
            return NULL;
        fast = fast->next->next;
        slow = slow->next;
    }while(fast != slow);
    fast = head;
    while(fast != slow)
    {
        fast = fast->next;
        slow = slow->next;
    }
    return fast;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
