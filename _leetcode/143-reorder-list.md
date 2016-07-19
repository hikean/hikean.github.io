---
layout: leetcode
date: 2016-07-13
title: Reorder List
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a singly linked list L: L0→L1→…→Ln-1→Ln,
>
>reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
>
>You must do this in-place without altering the nodes' values.
>
>For example,
>
>Given `{1,2,3,4}`, reorder it to `{1,4,2,3}`.
>
>     

***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode * reverse(struct ListNode * head)
{
    struct ListNode Head,*tmp;
    Head.next = NULL;
    while(head)
    {
        tmp = head;
        head = head->next;
        tmp->next = Head.next;
        Head.next = tmp;
    }
    return Head.next;
}
void reorderList(struct ListNode* head) {
    struct ListNode Head,*fast,*slow,*last;
    Head.next = head;
    last = &Head;
    slow = fast = head;
    while(fast && fast->next)
    {
        fast = fast->next->next;
        slow = slow->next;
    }
    if(fast)
    {
        fast = slow;
        slow = slow->next;
        fast->next = NULL;
    }
    slow = reverse(slow);
    while(slow)
    {
        last->next = head;
        last = head;
        head = head->next;
        last->next = slow;
        last = slow;
        slow = slow ->next;
    }
    last->next = fast;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
