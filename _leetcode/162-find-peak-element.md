---
layout: leetcode
date: 2016-07-15
title: Find Peek Element
tags: [Binary Search, Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

**Note:**

Your solution should be in logarithmic complexity.
    

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int N = nums.size();
        if (N == 1)
            return 0;
        int left = 0, right = N - 1;
        while (right - left > 1) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[mid + 1])
                left = mid + 1;
            else
                right = mid;
        }
        return (left == N - 1 || nums[left] > nums[left + 1]) ? left : right;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
