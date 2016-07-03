---
layout: leetcode
date: 2016-06-27
title: Permutations II
tags: [Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a collection of numbers that might contain duplicates, return all possible unique permutations.
>
>For example,
>
>`[1,1,2]` have the following unique permutations:
>    
>     [
>       [1,1,2],
>       [1,2,1],
>       [2,1,1]
>     ]
>

***

## Solution

**Result:** Accepted **Time:** 31 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ret;
        sort(nums.begin(),nums.end());
        do{
            ret.push_back(nums);
        }while(next_permutation(nums.begin(),nums.end()));
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n!)$$
- Space Complexity: $$O(n!)$$
