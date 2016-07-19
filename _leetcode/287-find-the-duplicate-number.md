---
layout: leetcode
date: 2016-07-17
title: Find the Duplicate Number
tags: [Binary Search, Array, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

**Note:**

1. You **must not** modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than <code>O(n<sup>2</sup>)</code>.
4. There is only one duplicate number in the array, but it could be repeated more than once.



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
int findDuplicate(int* nums, int numsSize) {
    for(int i = 0; i < numsSize; i++)
    {
        int idx = i;
        while(nums[idx] - 1 != idx)
        {
            int  tmp = nums[nums[idx] - 1];
            if(tmp == nums[idx])
                return tmp;
            nums[nums[idx] - 1] = nums[idx];
            nums[idx] = tmp;
            idx = tmp - 1;
        }
    }
    return 0;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
