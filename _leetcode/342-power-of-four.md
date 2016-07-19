---
layout: leetcode
date: 2016-07-18
title: Power of Four
tags: [Math, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

**Example:**

Given num = 16, return true. Given num = 5, return false.

**Follow up:** Could you solve it without `loops`/`recursion`?



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
bool isPowerOfFour(int num) {
    return num > 0 && num == (num&(-num)) && !(num & 0xaaaaaaaa);
}
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
