---
layout: leetcode
date: 2016-07-17
title: Remove Duplicate Letters
tags: [Stack, Greedy]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

**Example:**

Given `"bcabc"`

Return `"abc"`

Given `"cbacdcbc"`

Return `"acdb"`



***

## Solution

**Result:** Accepted **Time:**  0 ms

Here should be some explanations.

```c
char* removeDuplicateLetters(char* s) {
    int chrs[256]={0},cnt = -1;
    bool used[256]={0};
    char * str = s;
    while(*str) chrs[*(str++)]++;
    str = s;
    while(*str)
    {
        chrs[*str]--;
        if(!used[*str])
        {
            while(cnt >= 0 && chrs[s[cnt]] > 0 && *str < s[cnt]) 
                used[s[cnt--]] = false;
            s[++cnt] = *str;
            used[*str] = true;
        }
        ++str;
    }
    s[++cnt] = '\0';
    return s;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$

