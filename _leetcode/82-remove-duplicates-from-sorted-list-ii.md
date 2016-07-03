---
layout: leetcode
date: 2016-06-28
title: Remove Duplicates from Sorted List II
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
>
>For example,
>
>Given `1->2->3->3->4->4->5`, return `1->2->5`.
>
>Given `1->1->1->2->3`, return `2->3`.
>

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(!head) return NULL;
    struct ListNode Head,*last,*tmp;
    tmp = last = &Head;
    Head.next = NULL;
    Head.val = head -> val - 1;
    while(head)
    {
        if(head->val != tmp->val && (!head->next || (head->next && head->val != head->next->val)))
        {
            last->next = head;
            last = head;
        }
        tmp = head;
        head = head->next;
    }
    last->next = NULL;
    return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
