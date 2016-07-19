---
layout: leetcode
date: 2016-07-16
title: Invert Binary Tree
tags: [Tree]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Invert a binary tree.

<pre>         4
       /   \
      2     7
     / \   / \
    1   3 6   9
 </pre>

to

<pre>         4
       /   \
      7     2
     / \   / \
    9   6 3   1
</pre>


**Trivia:**

This problem was inspired by this original tweet by Max Howell:

> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.


***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL )
            return root;
        TreeNode * left = root->left;
        root -> left = invertTree(root->right);
        root -> right = invertTree(left);
        return root;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
