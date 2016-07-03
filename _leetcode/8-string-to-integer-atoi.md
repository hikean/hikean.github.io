---
layout: leetcode
date: 2016-06-23
title: String to Integer (atoi)
tags: [Math, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Implement atoi to convert a string to an integer.
>
> **Hint:** Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
>
> **Notes:** It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
>

***

## Solution

**Result:** Accepted **Time:** 4ms

Here should be some explanations.

```c
int myAtoi(char* str) {
    const long long limit = 0x7fffffff;
    long long ans = 0;
    if(str == NULL)
        return 0;
    int idx = 0;
    while(str[idx] != '\n')
        if(str[idx] ==' ' || str[idx] == '\n' || str[idx] == '\t')
            idx++;
        else
            break;
    int st = idx;
    if(str[idx] =='+' || str[idx] == '-')
        st = idx + 1;
    for(; isdigit(str[st]) && st < 12+idx; st++)
    {
        ans = ans*10 + (long long)(str[st] - '0');
    }
    if(str[idx] != '-' && ans > limit)
        return 0x7fffffff;
    if(str[idx] == '-' && ans > limit + 1)
        return 0x80000000;
    if(str[idx] == '-')
        return (int) -ans;
    return (int)(ans);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
