---
layout: leetcode
date: 2016-07-11
title: Validate Binary Search Tree
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, determine if it is a valid binary search tree (BST).
>
>Assume a BST is defined as follows:
>
>  - The left subtree of a node contains only nodes with keys **less than** the node's key.
>
>  - The right subtree of a node contains only nodes with keys **greater than** the node's key.
>
>  - Both the left and right subtrees must also be binary search trees.
>
>**Example 1:**
>
>        2
>       / \
>      1   3
>     
>Binary tree `[2,1,3]`, return true.
>
>**Example 2:**
>
>        1
>       / \
>      2   3
>    
> Binary tree `[1,2,3]`, return false.
>

***


## Solution

**Result:** Accepted **Time:** 8 ms

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
bool is_set;
int before = INT_MIN;
bool dfs(struct TreeNode * root)
{
    if(root == NULL) return true;
    if(dfs(root->left))
    {
        if(is_set && root -> val <= before)
            return false;
        is_set = true;
        before = root->val;
        return dfs(root->right);
    }
    return false;
}
bool isValidBST(struct TreeNode* root){
    is_set = false;
    return dfs(root);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
