---
layout: leetcode
date: 2016-07-11
title: Binary Tree Zigzag Level Order Traversal
tags: [Tree, Stack, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
>
>For example:
>
>Given binary tree `[3,9,20,null,null,15,7]`,
>
>         3
>        / \
>       9  20
>         /  \
>        15   7
>
>return its zigzag level order traversal as:
>
>     [
>       [3],
>       [20,9],
>       [15,7]
>     ]
>
>

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        queue<TreeNode * > que;
        queue<int> ique;
        vector<vector<int>> ret;
        que.push(root),ique.push(0);
        while(!que.empty())
        {
            int lv = ique.front();ique.pop();
            root = que.front();que.pop();
            if(root)
            {
                if(ret.size() <= lv)
                    ret.push_back(vector<int>());
                ret[lv].push_back(root->val);
                ique.push(lv+1);ique.push(lv+1);
                que.push(root->left);que.push(root->right);
            }
        }
        for(int i = 0; i < ret.size(); i++)
            if(i&1)
                reverse(ret[i].begin(),ret[i].end());
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
