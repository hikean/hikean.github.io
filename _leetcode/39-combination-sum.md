---
layout: leetcode
date: 2016-06-26
title: Combination Sum
tags: [Array, Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a set of candidate numbers (**C**) and a target number (**T**), find all unique combinations in **C** where the candidate numbers sums to **T**.
>
>The same repeated number may be chosen from **C** unlimited number of times.
>
>**Note:**
>
>  - All numbers (including target) will be positive integers.
>
>  - The solution set must not contain duplicate combinations.
>
>For example, given candidate set `[2, 3, 6, 7]` and target `7`,
>
>A solution set is:
>
>     [
>       [7],
>       [2, 2, 3]
>     ]
>     

***

## Solution

**Result:** Accepted **Time:** 20ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(vector<int> & cdd,vector<int> &sol,vector< vector<int>> &ret,int ptr,int rest)
    {
        if(!rest)
            return ret.push_back(sol);
        if(ptr >= cdd.size()) return ;
        dfs(cdd,sol,ret,ptr+1,rest);
        int i;
        for(i = 0 ; rest >= cdd[ptr];i++)
        {
            sol.push_back(cdd[ptr]);
            rest -= cdd[ptr];
            dfs(cdd,sol,ret,ptr+1,rest);
        }
        while(i--) sol.pop_back();
    }
    vector<vector<int>> combinationSum(vector<int>& cdd, int target) {
        vector<vector<int>> ret;
        vector<int> sol;
        sort(cdd.begin(),cdd.end());
        dfs(cdd,sol,ret,0,target);
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n!)$$
- Space Complexity: $$O(n)$$?
