---
layout: leetcode
date: 2016-06-26
title: Next Permutation
tags: [Array, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
>
>If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
>
>The replacement must be in-place, do not allocate extra memory.
>
>Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
>
> `1,2,3` → `1,3,2`
>
> `3,2,1` → `1,2,3`
>
> `1,1,5` → `1,5,1`
>
>


***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        const int sz = nums.size();
        int i = sz - 1,j = sz,t;
        while(i  && nums[i - 1] >= nums[i]) i--;
        if(i)
        {
            t = nums[sz - 1] > nums[i - 1] ? sz - 1:i;
            while(--j >= i)
                if(nums[j] < nums[t] && nums[j] > nums[i -1])
                    t = j;
            j = nums[i - 1];
            nums[i - 1] = nums[t];
            while( ++t < sz && j < nums[t])
                nums[t- 1] = nums[t];
            nums[t - 1] = j;
        }
        reverse(nums.begin() + i, nums.end());
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
