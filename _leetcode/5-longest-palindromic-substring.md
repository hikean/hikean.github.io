---
layout: leetcode
date: 2016-06-23
title: Longest Palindromic Substring
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
>


***

## Solution

**Result:** Accepted **Time:** 4ms

Manacher Algorithm should be the best way to solve this. However I choose a easy way.

```c
char* longestPalindrome(char* s) {
    const int slen = strlen(s);
    int len = 0,mid = 0,tmp,i,j,k;
    for(int t = 0,m = slen >> 1; t <= slen + 1; t++)
    {
        k = m + ((t&1)?-(t>>1):(t>>1));
        for(i = k, j = k + 1, tmp = 0; j < slen &&s[i]==s[j]; i--,j++)
            tmp +=2;
        if(tmp > len)
            len = tmp,mid = k;
        for(i = k - 1, j = k + 1, tmp = 1; j < slen &&s[i]==s[j]; i--,j++)
            tmp +=2;
        if(tmp > len)
            len = tmp,mid = k;
        if(len / 2  > slen - k) break;
    }
    char * ret = malloc(sizeof(char)*(len + 2));
    for(int i = 0,j = mid - ((len-1)>>1); i < len; ret[i++] = s[j++]);
    ret[len] = 0;
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
