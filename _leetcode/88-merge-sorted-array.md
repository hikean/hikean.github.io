---
layout: leetcode
date: 2016-07-07
title: Merge Sorted Array
tags: [Array, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two sorted integer arrays *nums1* and *nums2*, merge *nums2* into *nums1* as one sorted array.
>
> **Note:**
>
>You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
>
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
void merge(int* nums1, int m, int* nums2, int n) {
    int *ptr=m+n+nums1 ;
    while(m && n) *(--ptr) = nums1[m-1] > nums2[n-1]? nums1[--m]: nums2[--n];
    while(n)  *(--ptr) = nums2[--n];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
