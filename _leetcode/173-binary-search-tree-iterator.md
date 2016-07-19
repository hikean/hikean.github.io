---
layout: leetcode
date: 2016-07-16
title: Binary Search Tree Iterator
tags: [Tree, Stack, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling `next()` will return the next smallest number in the BST.

**Note:** `next()` and `hasNext()` should run in average $$O(1)$$ time and uses $$O(h)$$ memory, where h is the height of the tree.


***

## Solution

**Result:** Accepted **Time:** 32 ms

Here should be some explanations.

```cpp
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
    vector<TreeNode*> stck;
public:
    BSTIterator(TreeNode *root) {
        while(root)
        {
             stck.push_back(root);
             root = root->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return stck.size() > 0;
    }

    /** @return the next smallest number */
    int next() {
        TreeNode * tmp = stck.back();
        stck.pop_back();
        int ret = tmp->val;
        tmp = tmp->right;
        while(tmp)
        {
            stck.push_back(tmp);
            tmp = tmp->left;
        }
        return ret;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(h)$$
