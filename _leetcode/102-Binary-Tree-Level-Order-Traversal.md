---
layout: leetcode
date: 2016-07-11
title: Binary Tree Level Order Traversal
tags: [Tree, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
>
>For example:
>
>Given binary tree `[3,9,20,null,null,15,7]`,
>
>        3
>       / \
>      9  20
>        /  \
>       15   7
>
>return its level order traversal as:
>
>     [
>       [3],
>       [9,20],
>       [15,7]
>     ]
>     

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int get_depth(struct TreeNode * root)
    {
        if(root == NULL) return 0;
        int a = get_depth(root->left)+1;
        int b = get_depth(root->right)+1;
        return a>b?a:b;
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        int now = 0,depth = get_depth(root);
        vector<vector<int> > ans(depth);
        TreeNode *cur=NULL;
        queue<int> level;
        queue<TreeNode*> nodes;
        nodes.push(root);
        level.push(0);
        while(!nodes.empty())
        {
            cur = nodes.front();nodes.pop();
            now = level.front();level.pop();
            if(cur != NULL)
            {
                ans[now].push_back(cur->val);
                nodes.push(cur->left),level.push(now+1);
                nodes.push(cur->right),level.push(now+1);
            }
        }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
