---
layout: leetcode
date: 2016-07-16
title: Combination Sum III
tags: [Array, Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


**Example 1:**

 Input: k = 3, n = 7

Output:

<pre>
     [[1,2,4]]
</pre>

**Example 2:**

Input: k = 3, n = 9

Output:

<pre>
     [[1,2,6], [1,3,5], [2,3,4]]
</pre>

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(int rest,int st,int k,vector<vector<int>> &vec,vector<int> &ivec)
    {
        if(!rest && !k)
            return vec.push_back(ivec);
        int limit = (2*st+k-1)*k/2;
        if(k == 1) st = rest;
        for(int i = st; limit <= rest && i < 10; i++,limit +=k)
        {
            ivec.push_back(i);
            dfs(rest - i,i+1,k-1,vec,ivec);
            ivec.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> vec;
        vector<int> ivec;//(k);
        dfs(n,1,k,vec,ivec);
        return vec;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
