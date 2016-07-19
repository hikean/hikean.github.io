---
layout: leetcode
date: 2016-07-16
title: Kth Largest Element in an Array
tags: [Heap, Divide and Conquer]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Find the **k**<sup>th</sup> largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,

Given ``[3,2,1,5,6,4]`` and k = 2, return 5.

**Note:**

You may assume k is always valid, 1 ≤ k ≤ array's length.


***

## Solution

**Result:** Accepted **Time:** 20 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        return nums[nums.size()-k];
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(1)$$
