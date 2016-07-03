---
layout: leetcode
date: 2016-06-26
title: Combination Sum II
tags: [Array, Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a collection of candidate numbers (**C**) and a target number (**T**), find all unique combinations in **C** where the candidate numbers sums to **T**.
>
>Each number in **C** may only be used **once** in the combination.
>
>**Note:**
>
>  - All numbers (including target) will be positive integers.
>  - The solution set must not contain duplicate combinations.
>
>For example, given candidate set `[10, 1, 2, 7, 6, 1, 5]` and target `8`,
>
>A solution set is:
>
>     [
>       [1, 7],
>       [1, 2, 5],
>       [2, 6],
>       [1, 1, 6]
>     ]
>     

***

## Solution

**Result:** Accepted **Time:** 12ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(vector<int> & cdd,vector<int> &sol,vector< vector<int>> &ret,int ptr,int rest)
    {
        if(!rest)
            return ret.push_back(sol);
        if(ptr >= cdd.size() || rest < 0) return ;
        int last = ptr,i;
        while(++last < cdd.size() && cdd[ptr] == cdd[last]);
        dfs(cdd,sol,ret,last,rest);
        for(i = 0;rest >= cdd[ptr] && i+ptr < last;i++)
        {
            sol.push_back(cdd[ptr]);
            rest -= cdd[ptr];
            dfs(cdd,sol,ret,last,rest);
        }
        while(i--)
            sol.pop_back();
    }
    vector<vector<int>> combinationSum2(vector<int>& cdd, int target) {
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
