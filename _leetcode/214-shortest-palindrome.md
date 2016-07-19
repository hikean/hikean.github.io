---
layout: leetcode
date: 2016-07-16
title: Shortest Palindrome
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a string **S**, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given ``"aacecaaa"``, return ``"aaacecaaa"``.

Given ``"abcd"``, return ``"dcbabcd"``.
     

***

## Solution

**Result:** Accepted **Time:** 765 ms

Here should be some explanations.

```c
char* shortestPalindrome(char* s) {
    const int slen = strlen(s);
    int i = 0, j = 0, k;
    for(k = slen - 1; k >= 0 && i <= j; k--)
        for(i = 0, j= k; i <= j && s[i]==s[j]; i++,j--);
    char * ret = malloc(sizeof(char)*(slen * 2));
    for(i = 0; i + k < slen - 2;i++)
        ret[i] = s[slen-1-i];
    strcpy(ret+i,s);
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
