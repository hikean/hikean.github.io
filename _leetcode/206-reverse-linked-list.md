---
layout: leetcode
date: 2016-07-16
title: Reverse Linked List
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


 Reverse a singly linked list.

 **Hint:**

 A linked list can be reversed either iteratively or recursively. Could you implement both?



***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode * top = NULL,* tmp;
    while(head)
    {
        tmp = head->next;
        head->next = top;
        top = head;
        head = tmp;
    }
    return top;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
