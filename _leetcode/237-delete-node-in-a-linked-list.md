---
layout: leetcode
date: 2016-07-16
title: Delete Node in a Linked List
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is `1 -> 2 -> 3 -> 4` and you are given the third node with value 3, the linked list should become `1 -> 2 -> 4` after calling your function.


***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode * tmp = node->next;
    node->val = tmp->val;
    node->next = tmp->next;
    free(tmp);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
