---
layout: leetcode
date: 2016-07-11
title: Symmetric Tree
tags: [Tree, Depth First Search, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
>
>For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:
>
>         1
>       / \
>       2   2
>      / \ / \
>     3  4 4  3
>     
>
> But the following `[1,2,2,null,3,null,3]` is not:
>
>        1
>       / \
>      2   2
>       \   \
>       3    3
>
> **Note:**
>
> Bonus points if you could solve it both recursively and iteratively.

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
bool _is_symmetric(struct TreeNode * r1,struct TreeNode * r2)
{
    if(r1 == r2 && r1 == NULL)
        return true;
    if(!r1 || !r2)
        return false;
    if(r1->val != r2->val)
        return false;
    return _is_symmetric(r1->left,r2->right) && _is_symmetric(r1->right,r2->left);
}

bool isSymmetric(struct TreeNode* root) {
    if(root == NULL) return true;
    return _is_symmetric(root->left,root->right);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
