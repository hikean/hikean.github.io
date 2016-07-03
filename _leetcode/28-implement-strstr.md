---
layout: leetcode
date: 2016-06-25
title: Implement strStr()
tags: [Two Pointers, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Implement strStr().
>
>Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
>


***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
int strStr(char* haystack, char* needle) {
    int i = 0, j = 0 ,len;
    while(haystack[i])
    {
        j = 0;
        len = 0;
        while(haystack[i+j] && needle[j]==haystack[i+j])
        {
            j++;
            if(len >= 0 && needle[j]==needle[j-1])
                len++;
            else
                len = -len;
        }
        if(!needle[j])
            return i;
        i++;
        if(len < -10)
            i -= len;
    }
    if( needle[0] =='\0')
        return 0;
    return -1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(m*n)$$
- Space Complexity: $$O(1)$$
