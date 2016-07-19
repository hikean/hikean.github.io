---
layout: leetcode
date: 2016-07-16
title: Rotate Array
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

**Note:**

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

**Hint:**

Could you do it in-place with O(1) extra space?


***

## Solution

**Result:** Accepted **Time:** 24 ms

Here should be some explanations.

```cpp
class Solution {
    void reverse(vector<int>& nums,int i,int k)
    {
        int tmp ;
        while(i<k)
        {
            tmp = nums[i];
            nums[i++] = nums[k];
            nums[k--] = tmp;
        }

    }
public:
    void rotate(vector<int>& nums, int k) {
        k = k%(nums.size());
        if(!k) return ;
        reverse(nums,0,nums.size()-k-1);
        reverse(nums,nums.size()-k,nums.size()-1);
        reverse(nums,0,nums.size()-1);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
