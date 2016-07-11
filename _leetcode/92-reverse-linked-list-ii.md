---
layout: leetcode
date: 2016-07-07
title: Reverse Linked List II
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Reverse a linked list from position m to n. Do it in-place and in one-pass.
>
>For example:
>Given `1->2->3->4->5->NULL`, m = 2 and n = 4,
>
>return `1->4->3->2->5->NULL`.
>
>**Note:**
>
>Given m, n satisfy the following condition:
>
>1 ≤ m ≤ n ≤ length of list.
>
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
    if(m == n)
        return head;
    struct ListNode Head;
    Head.next = head;
    struct ListNode * now = head, *last = &Head,*tmp;
    struct ListNode ptr;
    ptr.next = NULL;
    int cnt = 1;
    while(cnt < m)
    {
        last = now;
        now = now -> next;
        cnt++;
    }
    while(cnt <= n)
    {
        tmp = now;
        now = now->next;
        tmp -> next  = ptr.next;
        ptr.next = tmp;
        cnt++;
    }
    last->next -> next = now;
    last->next = ptr.next;
    return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
