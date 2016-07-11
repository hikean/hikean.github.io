---
layout: leetcode
date: 2016-07-11
title: Same Tree
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two binary trees, write a function to check if they are equal or not.
>
> Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
>

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if(p && q && p->val == q->val)
        return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
    return p == q;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
