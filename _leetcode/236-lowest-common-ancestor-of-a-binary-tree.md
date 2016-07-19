---
layout: leetcode
date: 2016-07-16
title: Lowest Common Ancestor of a Binary Tree
tags: [Tree]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to [the definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (**where we allow a node to be a descendant of itself**).”

<pre>
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
</pre>
For example, the lowest common ancestor (LCA) of nodes `5` and `1` is `3`. Another example is LCA of nodes `5` and `4` is `5`, since a node can be a descendant of itself according to the LCA definition.



***

## Solution

**Result:** Accepted **Time:** 16 ms

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
    if(!root || root == p || root == q)  
            return root;
    struct TreeNode* left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if(left)
        return right?root:left;
    return right;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
