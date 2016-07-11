---
layout: leetcode
date: 2016-07-07
title: Unique Binary Search Tree II
tags: [Tree, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an integer n, generate all structurally unique **BST**'s (binary search trees) that store values 1...n.
>
>For example,
>
>Given n = 3, your program should return all 5 unique BST's shown below.
>
>         1         3     3      2      1
>          \       /     /      / \      \
>           3     2     1      1   3      2
>          /     /       \                 \
>         2     1         2                 3
>     

***

## Solution

**Result:** Accepted **Time:** 28 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<TreeNode*> dfs(int left,int right)
    {
        if(left >= right)
            return vector<TreeNode*>{NULL};
        vector<TreeNode*> ret;
        for(int i = left; i < right; i++)
        {
            vector<TreeNode*> lvect = dfs(left,i);
            vector<TreeNode*> rvect = dfs(i+1,right);
            for(const auto &lft:lvect)
                for(const auto & rht:rvect)
                {
                    TreeNode * tmp = new TreeNode(i);
                    tmp->left = lft;
                    tmp->right = rht;
                    ret.push_back(tmp);
                }
        }
        return ret;
    }
    vector<TreeNode*> generateTrees(int n) {
        if(!n) return vector<TreeNode*>();
        return dfs(1,n+1);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n!)$$?
- Space Complexity: $$O(n!)$$?
