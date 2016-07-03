---
layout: leetcode
date: 2016-06-28
title: Add Binary
tags: [Math, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two binary strings, return their sum (also a binary string).
>
>For example,
>
>a = `"11"`
>
>b = `"1"`
>
>Return `"100"`.
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
char* addBinary(char* a, char* b) {
    int lena = strlen(a), lenb = strlen(b), carry = 0;
    int lenc = lena > lenb?lena:lenb;
    char * c = malloc(lenc+2);
    c[lenc+1] = '\0';
    while(lena || lenb ){
        if(lena) carry += (a[--lena]-'0');
        if(lenb) carry += (b[--lenb]-'0');
        c[lenc--] = (carry&1)+'0';
        carry >>= 1;
    }
    c[0] = carry+'0';
    return c+(carry^1);
    //for(int i = -1, j = 0;c[j] && !carry;c[++i] = c[++j]);
    //return c;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
