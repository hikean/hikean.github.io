---
layout: leetcode
date: 2016-06-26
title: Search for A Range
tags: [Array, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a sorted array of integers, find the starting and ending position of a given target value.
>
>Your algorithm's runtime complexity must be in the order of $$O(log(n))$$.
>
>If the target is not found in the array, return `[-1, -1]`.
>
>For example,
>
>Given `[5, 7, 7, 8, 8, 10]` and target value `8`,
>
>return `[3, 4]`.
>
>

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int low = 0,up = nums.size() - 1,mid,a,b;
        while(low <= up)
        {
            mid = (low + up)/2;
            if(nums[mid] >= target)
                up = mid -1;
            else
                low = mid + 1;
        }
        a = low;
        up = nums.size()-1;
        while(low <= up)
        {
            mid = (low + up)/2;
            if(nums[mid] > target)
                up = mid -1;
            else
                low = mid + 1;
        }
        b = up;
        if(nums[a]!= target) a=b=-1;
        return vector<int>{a,b};
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
