---
layout: leetcode
date: 2016-07-11
title: Construct Binary Tree from Inorder and Postorder traversal
tags: [Tree, Array, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given inorder and postorder traversal of a tree, construct the binary tree.
>
>**Note:**
>
>You may assume that duplicates do not exist in the tree.
>     

***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```c
struct TreeNode * build(int * in,int *post,int left,int right,int *ptr)
{
    if(left >= right || *ptr < 0)
        return NULL;
    int mid = left;
    while(post[*ptr] != in[mid]) mid++;
    struct TreeNode * root = malloc(sizeof(struct TreeNode));
    root->val = post[(*ptr)--];
    root->right = build(in,post,mid+1,right,ptr);
    root->left = build(in,post,left,mid,ptr);
    return root;
}
struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    int ptr = inorderSize-1;
    return build(inorder,postorder,0,postorderSize,&ptr);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
