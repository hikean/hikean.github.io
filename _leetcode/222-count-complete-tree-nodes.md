---
layout: leetcode
date: 2016-07-16
title: Count Complete Tree Nodes
tags: [Tree, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a **complete** binary tree, count the number of nodes.

<u>Definition of a complete binary tree from <a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees"><b>Wikipedia:</b></a></u>

In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between $$1$$ and $$2^h$$ nodes inclusive at the last level h.


***

## Solution

**Result:** Accepted **Time:** 176 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int helper(TreeNode * root)
    {
        if(!root)
            return 0;
        int leftside=0, rightside=0;
        TreeNode *l=root, *r=root;
        while(l) leftside++,l=l->left;
        while(r) rightside++, r=r->right;
        if(rightside==leftside)
            return (1 << rightside)-1;
        return helper(root->left)+helper(root->right)+1;
    }
    int countNodes(TreeNode* root) {
        return helper(root);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
