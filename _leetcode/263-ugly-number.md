---
layout: leetcode
date: 2016-07-16
title: Ugly Number
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include `2, 3, 5`. For example, `6, 8` are ugly while `14` is not ugly since it includes another prime factor `7`.

Note that `1` is typically treated as an ugly number.


***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
bool isUgly(int num) {
    if(num <= 0)
        return false;
    while(num && num % 3 == 0)
        num /= 3;
    while(num && num % 5 == 0)
        num /= 5;
    while(num && num % 2 == 0)
        num /= 2;
    return num == 1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
