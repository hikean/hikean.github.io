---
layout: leetcode
date: 2016-07-11
title: Path Sum
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
>
>For example:
>
>Given the below binary tree and `sum = 22`,
>
>                   5
>                  / \
>                 4   8
>                /   / \
>               11  13  4
>              /  \      \
>             7    2      1
>
> return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
bool hasPathSum(struct TreeNode* root, int sum) {
    if(root == NULL)
        return false;
    if(root -> left == NULL && root->right == NULL)
        return root->val == sum;
    return hasPathSum(root->left,sum-root->val) || hasPathSum(root->right,sum-root->val);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
