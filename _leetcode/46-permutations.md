---
layout: leetcode
date: 2016-06-26
title: Permutations
tags: [Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a collection of distinct numbers, return all possible permutations.
>
> For example,
>
>`[1,2,3]` have the following permutations:
>
>     [
>       [1,2,3],
>       [1,3,2],
>       [2,1,3],
>       [2,3,1],
>       [3,1,2],
>       [3,2,1]
>     ]
>     

***

## Solution

**Result:** Accepted **Time:** 16ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(vector<int> & ivec,const vector<int> & nums,vector<vector<int>> & ret,bool used[],const int cnt)
    {
        if(ivec.size() == cnt)
            return ret.push_back(ivec);
        for(int i = 0; i < cnt; i++)
            if(!used[i])
            {
                used[i] = true;
                ivec.push_back(nums[i]);
                dfs(ivec,nums,ret,used,cnt);
                ivec.pop_back();
                used[i] = false;
            }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> ivec;
        vector<vector<int>> ret;
        bool used[16]={0};
        dfs(ivec,nums,ret,used,nums.size());
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n!)$$
- Space Complexity: $$O(n!)$$
