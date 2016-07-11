---
layout: leetcode
date: 2016-07-11
title: Balanced Binary Tree
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, determine if it is height-balanced.
>
>For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
>
>   

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int depth(struct TreeNode * root)
{
    if(root == NULL)
        return 0;
    int a = depth(root->left);
    int b = depth(root->right);
    if(a-b < - 1 || a - b > 1)
        return 0x0fffffff;
    return (a>b?a:b) + 1;
}
bool isBalanced(struct TreeNode* root) {
    return depth(root) < 0x0fffffff;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
