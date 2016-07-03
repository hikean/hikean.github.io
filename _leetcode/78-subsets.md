---
layout: leetcode
date: 2016-06-28
title: Subsets
tags: [Array, Backtracking, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a set of distinct integers, nums, return all possible subsets.
>
>**Note:** The solution set must not contain duplicate subsets.
>
>For example,
>
>If **nums** = `[1,2,3]`, a solution is:
>
>     [
>       [3],
>       [1],
>       [2],
>       [1,2,3],
>       [1,3],
>       [2,3],
>       [1,2],
>       []
>     ]
>
>

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        int len = 1<<nums.size();
        for(int i = 0 ; i < len; i++ )
            {
                int tmp = i;
                vector<int> vec;
                for(int j = 0;tmp;j++ )
                    {
                        if(tmp & 1)
                            vec.push_back(nums[j]);
                        tmp >>= 1;
                    }
                ans.push_back(vec);
            }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(2^n)$$
- Space Complexity: $$O(2^n)$$
