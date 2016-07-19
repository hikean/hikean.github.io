---
layout: leetcode
date: 2016-07-16
title:  Lowest Common Ancestor of a Binary Search Tree
tags: [Tree]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (**where we allow a node to be a descendant of itself**).”

<pre>
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
</pre>

For example, the lowest common ancestor (LCA) of nodes `2` and `8` is `6`. Another example is LCA of nodes `2` and `4` is `2`, since a node can be a descendant of itself according to the LCA definition.



***

## Solution

**Result:** Accepted **Time:** 24 ms

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
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if(p->val > root-> val && q->val > root->val)
        return lowestCommonAncestor(root->right,p,q);
    if(p->val < root-> val && q->val < root->val)
        return lowestCommonAncestor(root->left,p,q);
    return root;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
