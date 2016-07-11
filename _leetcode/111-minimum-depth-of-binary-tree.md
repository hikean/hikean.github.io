---
layout: leetcode
date: 2016-07-11
title: Minimum Depth of Binary Tree
tags: [Tree, Depth First Search, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, find its minimum depth.
>
>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
>
>

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int minDepth(struct TreeNode* root) {
    if(root == NULL)
        return 0;
    if(!root->left && !root->right)
        return 1;
    int a = 0x07fffffff,b = 0x7fffffff;
    if(root->left)
        a = minDepth(root->left);
    if(root->right)
        b = minDepth(root->right);
    return (a>b?b:a)+1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
