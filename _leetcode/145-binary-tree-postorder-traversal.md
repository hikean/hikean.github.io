---
layout: leetcode
date: 2016-07-13
title: Binary Tree Postorder Traversal
tags: [Tree, Stack]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, return the postorder traversal of its nodes' values.
>
>For example:
>
>Given binary tree `{1,#,2,3}`,
>
>        1
>         \
>          2
>         /
>        3
>    
>return `[3,2,1]`.
>
>**Note:** Recursive solution is trivial, could you do it iteratively?
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

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
    vector<int> postorderTraversal(TreeNode* root) {
        stack<int> ista;
        stack<TreeNode*> tsta;
        vector<int> ret;
        TreeNode * tmp;
        int lev;
        tsta.push(root);
        ista.push(1);
        while(!tsta.empty())
        {
            tmp = tsta.top();tsta.pop();
            lev = ista.top();ista.pop();
            if(tmp == NULL) continue;
            if(lev == 2)
                ret.push_back(tmp->val);
            else
            {
                tsta.push(tmp),ista.push(2);
                tsta.push(tmp->right),ista.push(1);
                tsta.push(tmp->left),ista.push(1);
            }
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
