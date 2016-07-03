---
layout: leetcode
date: 2016-06-25
title: Remove Nth Node from End of List
tags: [Linked List, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a linked list, remove the $$n^{th}$$ node from the end of list and return its head.
>
>For example,
>
>     Given linked list: 1->2->3->4->5, and n = 2.
>     
>     After removing the second node from the end, the linked list becomes 1->2->3->5.
>
>**Note:**
>Given n will always be valid.
>
>Try to do this in one pass.    

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode Head,*ptr;
    Head.next = head;
    ptr = &Head;
    while(n--)
        head = head -> next;
    while(head)
    {
        head=head->next;
        ptr = ptr->next;
    }
    ///head = ptr ->next;
    /// free(head);
    ptr->next = ptr->next ->next;
    return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
