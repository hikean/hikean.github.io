---
layout: leetcode
date: 2016-07-11
title:  Convert Sorted List to Binary Search Tree
tags: [Depth First Search, Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
>

***

## Solution

**Result:** Accepted **Time:** 12 ms

Here should be some explanations.

```c
struct ListNode * current;
struct TreeNode * build_tree(int low,int up)
{
    if(low >= up ) return NULL;
    struct TreeNode * tmp = malloc(sizeof(struct TreeNode));
    int mid = low + ((up - low)>>1);
    tmp -> left = build_tree(low,mid);
    tmp -> val = current -> val;
    current = current -> next;
    tmp -> right = build_tree(mid+1,up);
    return tmp;
}

struct TreeNode* sortedListToBST(struct ListNode* head) {
    current = head;
    int len = 0;
    while(head)
        len++, head = head->next;
    return build_tree(0,len);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
