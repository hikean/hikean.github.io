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


```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode *> sta;
        vector<int> result;
        while(!sta.empty() || root){
            if(root == NULL)
            {
                root = sta.top();sta.pop();
                result.push_back(root->val);
                root = root->right;
            }
            else{
                while(root != NULL){
                    sta.push(root);
                    root = root->left;
                }
            }
        }
        return result;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
