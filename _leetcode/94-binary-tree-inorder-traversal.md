---
layout: leetcode
date: 2016-07-07
title: Binary Tree Inorder Traversal
tags: [Tree, Hash Table, Stack]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, return the inorder traversal of its nodes' values.
>
>For example:
>
>Given binary tree `[1,null,2,3]`,
>
>      1
>        \
>         2
>        /
>       3
>
>return [1,3,2].
>
>**Note:** Recursive solution is trivial, could you do it iteratively?
>


***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
/**
Just a recursive way -_-||.
**/
int *ptr;
int cnt;
void inorder_travel(struct TreeNode *root)
{
    if(root == NULL) return;
    inorder_travel(root->left);
    ptr[cnt++] = root->val;
    inorder_travel(root->right);
}
int node_count(struct TreeNode * root)
{   
    if(root == NULL) return 0;
    return node_count(root->left) + node_count(root->right) + 1;
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = node_count(root);
    ptr = malloc(sizeof(int) * (*returnSize)  + 2);
    cnt = 0;
    inorder_travel(root);
    return ptr;
}

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
