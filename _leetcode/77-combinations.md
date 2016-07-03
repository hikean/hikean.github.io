---
layout: leetcode
date: 2016-06-28
title: Combinations
tags: [Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
>
>For example,
>
>If n = 4 and k = 2, a solution is:
>
>     [
>       [2,4],
>       [3,4],
>       [2,3],
>       [1,2],
>       [1,3],
>       [1,4],
>     ]
>
>     

***

## Solution

**Result:** Accepted **Time:** 12 ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(vector<vector<int>> & ans,vector<int> &solu,int n,int k,int idx)
    {
        if(!k)  return  ans.push_back(solu);
        for(int i = idx; i <= n; i++)
        {
            solu.push_back(i);
            dfs(ans,solu,n,k-1,i+1);
            solu.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> solu;
        dfs(ans,solu,n,k,1);
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(C(n,k))$$
- Space Complexity: $$O(C(n,k))$$?
