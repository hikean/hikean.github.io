---
layout: leetcode
date: 2016-07-16
title: Power of Two
tags: [Math, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an integer, write a function to determine if it is a power of two.


***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
bool  isPowerOfTwo(const int n) {
    return  n > 0 &&n==((-n)&(n));
}
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
