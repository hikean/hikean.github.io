---
layout: leetcode
date: 2016-06-23
title: Palindrome Number
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Determine whether an integer is a palindrome. Do this without extra space.
>

***

## Solution

**Result:** Accepted **Time:** 60ms

Here should be some explanations.

```c
bool isPalindrome(int x) {
    if(x < 10)
        return x >= 0;
    if(x%10 ==0)
        return false;
    int y = 0,tmp;
    while(x > y)
    {
        tmp = x/10;
        if(tmp == y) return true;
        y = y*10 + (x%10);
        x = tmp;
    }
    return x==y;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(x))$$
- Space Complexity: $$O(1)$$
