---
layout: leetcode
date: 2016-07-18
title: Increasing Triplet Subsequence
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

> Return true if there exists i, j, k 
> such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Your algorithm should run in *O(n)* time complexity and *O(1)* space complexity.

**Examples:**

Given `[1, 2, 3, 4, 5]`,
return `true`.

Given `[5, 4, 3, 2, 1]`,
return `false`.



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
bool increasingTriplet(int* nums, int numsSize) {
    int min = nums[0], mid = 0x7fffffff;
    for(int i = 0; i < numsSize; i++ )
    {
        if(nums[i] < min)
            min = nums[i];
        else if(nums[i] > min)
        {
            if(nums[i] > mid)
                return true;
            mid = nums[i];
        }
    }
    return false;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
