---
layout: leetcode
date: 2016-07-16
title: Remove Linked List Elements
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Remove all elements from a linked list of integers that have value **val**.

**Example:**

**Given:** 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, **val** = 6

**Return:** 1 --> 2 --> 3 --> 4 --> 5

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* last;
    struct ListNode* now;
    struct ListNode first;
    last = &first;
    now = head;
    first.val = val + 1;
    first.next = head;
    while(now)
    {
        if(now -> val == val)
        {
            last -> next = now -> next;
            free(now);
        }
        else
        {
            last = now;
        }
        now = last -> next;
    }
    return first . next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
