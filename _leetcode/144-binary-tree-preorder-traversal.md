---
layout: leetcode
date: 2016-07-13
title: Binary Tree Preorder Traversal
tags: [Tree, Stack]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, return the preorder traversal of its nodes' values.
>
>For example:
>Given binary tree {1,#,2,3},
>
>        1
>         \
>          2
>         /
>        3
>
>return `[1,2,3]`.
>
>Note: Recursive solution is trivial, could you do it iteratively?
>
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

int *ptr;
int cnt;
void inorder_travel(struct TreeNode *root)
{
    if(root == NULL) return;
    ptr[cnt++] = root->val;
    inorder_travel(root->left);
    inorder_travel(root->right);
}
int node_count(struct TreeNode * root)
{   
    if(root == NULL) return 0;
    return node_count(root->left) + node_count(root->right) + 1;
}
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = node_count(root);
    ptr = malloc(sizeof(int) * (*returnSize)  + 2);
    cnt = 0;
    inorder_travel(root);
    return ptr;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
