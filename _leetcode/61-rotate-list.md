---
layout: leetcode
date: 2016-06-28
title: Rotate List
tags: [Linked List, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a list, rotate the list to the right by k places, where k is non-negative.
>
>For example:
>
>Given `1->2->3->4->5->NULL` and `k = 2`,
>
>return `4->5->1->2->3->NULL`.
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(!k || !head)
        return head;
    struct ListNode * fast = head,*slow = head;
    int len = 0;
    while(fast)
        fast = fast->next,len++;
    for(fast = head,k = k % len; k; k--) //if(!k) return head;
        fast = fast->next;
    while(fast->next)
        fast = fast->next,slow = slow->next;
    fast -> next = head;
    head = slow->next;
    slow ->next = NULL;
    return head;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
