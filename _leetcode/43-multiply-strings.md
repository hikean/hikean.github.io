---
layout: leetcode
date: 2016-06-26
title: Multiply Strings
tags: [Math, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two numbers represented as strings, return multiplication of the numbers as a string.
>
> **Note:**
>
>  - The numbers can be arbitrarily large and are non-negative.
>  - Converting the input string to integer is **NOT** allowed.
>  - You should **NOT** use internal library such as **BigInteger**.
>     

***

## Solution

**Result:** Accepted **Time:** 4ms

Here should be some explanations.

```c
void reverse(char *s,int len)
{
    for(int i = 0, j = len -1;i < j; ++i, --j)
    {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}
char* multiply(char* a, char* b) {
    const int na = strlen(a), nb = strlen(b);
    reverse(a,na);
    reverse(b,nb);
    char *ans = malloc(sizeof(char)*(na+nb+4));
    memset(ans,0,sizeof(char)*(na+nb+4));
    for(int i = 0 ; i < na; i++)
    {
        int carry = 0;
        for(int j = 0; j < nb; j++)
        {
            carry += (a[i]-'0')*(b[j]-'0') + ans[i+j];
            ans[i+j] = carry % 10;
            carry /= 10;
        }
        for(int j = nb+i; carry; j++)
        {
            carry += ans[j];
            ans[j] = carry %10;
            carry /= 10;
        }
    }
    int len = na + nb + 2;
    while(len > 1 && !ans[len-1]) len--;
    for(int i = 0; i < len; i++)
        ans[i] += '0';
    reverse(ans,len);
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
