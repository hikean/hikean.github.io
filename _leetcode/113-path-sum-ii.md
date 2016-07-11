---
layout: leetcode
date: 2016-07-11
title: Path Sum II
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
>
>For example:
>
>Given the below binary tree and sum = 22,
>
>                   5
>                  / \
>                 4   8
>                /   / \
>               11  13  4
>              /  \    / \
>             7    2  5   1
>
> return
>
>     [
>        [5,4,11,2],
>        [5,8,4,5]
>     ]
>     
>

***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(TreeNode * root,const int sum,int now,vector<vector<int>> & ret,vector<int> & stck)
    {
        if(root==NULL)
            return ;
        now += root->val;
        stck.push_back(root->val);
        if(root->left == root->right && now == sum)
            ret.push_back(stck);
        else
        {
            dfs(root->left,sum,now,ret,stck);
            dfs(root->right,sum,now,ret,stck);
        }
        stck.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector< vector<int> > ret;
        vector<int> stck;
        dfs(root,sum,0,ret,stck);
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
