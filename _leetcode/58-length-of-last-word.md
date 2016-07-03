---
layout: leetcode
date: 2016-06-27
title: Length of Last Word
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string s consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.
>
>If the last word does not exist, return 0.
>
>**Note:** A word is defined as a character sequence consists of non-space characters only.
>
>For example,
>Given s = `"Hello World"`,
>return `5`.
>
>   

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
int lengthOfLastWord(char* s) {
    int len=0, last=0;
    while(*s)
    {
        if(*s == ' '  )
        {
            if(len)
                last = len;
            len=0;
        }
        else
            len++;
        s++;
    }
    return len==0?last:len;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
