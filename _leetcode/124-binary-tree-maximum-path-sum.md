---
layout: leetcode
date: 2016-07-11
title: Binary Tree Maximum Path Sum
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, find the maximum path sum.
>
>For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
>
>For example:
>
>Given the below binary tree,
>     
>            1
>           / \
>          2   3
>     
>
>Return `6`.
>     

***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```c
int ans;
int sum(struct TreeNode * root)
{
    if(root == NULL) return 0;
    int left = sum(root->left);
    int right = sum(root->right);
    int s = left + right + root->val;
    if(s > ans)
        ans = s;
    if(left < right)
        left = right;
    s = left + root->val;
    return s > 0 ? s : 0;
}
int maxPathSum(struct TreeNode* root) {
    ans = INT_MIN;//0x80000000;
    sum(root);
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
