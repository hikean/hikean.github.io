---
layout: leetcode
date: 2016-07-11
title: Construct Binary Tree from Preorder and Inorder Traversal
tags: [Tree, Array, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given preorder and inorder traversal of a tree, construct the binary tree.
>
>**Note:**
>
>You may assume that duplicates do not exist in the tree.
>


***

## Solution

**Result:** Accepted **Time:** 20 ms

Here should be some explanations.

```c
struct TreeNode * build(int * in,int *pre,const int isz,int left,int right,int *ptr)
{
    if(left >= right || *ptr >= isz)
        return NULL;
    int mid = left;
    while(pre[*ptr] != in[mid]) mid++;
    struct TreeNode * root = malloc(sizeof(struct TreeNode));
    root->val = pre[(*ptr)++];
    root->left = build(in,pre,isz,left,mid,ptr);
    root->right = build(in,pre,isz,mid+1,right,ptr);
    return root;
}
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    int ptr = 0;
    return build(inorder,preorder,inorderSize,0,inorderSize,&ptr);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
