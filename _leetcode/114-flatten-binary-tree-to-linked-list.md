---
layout: leetcode
date: 2016-07-11
title: Flatten Binary Tree to Linked List
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, flatten it to a linked list in-place.
>
>For example,
>
>Given
>
>examples
>
>          1
>         / \
>        2   5
>       / \   \
>      3   4   6
>        
>The flattened tree should look like:
>
>         1
>         \
>          2
>           \
>            3
>             \
>              4
>               \
>                5
>                 \
>                  6
>     





***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
struct TreeNode * flat(struct TreeNode* root)
{
    if(root == NULL)
        return NULL;
    struct TreeNode * right = root -> right;
    root->right = root->left;
    root->left = NULL;
    if(root->right)
        root = flat(root->right);
    if(right)
    {
        root->right = right;
        root = flat(right);
    }
    return root;
}
void flatten(struct TreeNode* root) {
    flat(root);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
