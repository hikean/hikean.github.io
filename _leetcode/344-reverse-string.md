---
layout: leetcode
date: 2016-07-18
title: Reverse String
tags: [String, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Write a function that takes a string as input and returns the string reversed.

**Example:**

Given s = `"hello"`, return `"olleh"`.



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
char* reverseString(char* s) {
    int low = 0;
    int up = strlen(s) -1;
    char tmp;
    while(low < up)
    {
        tmp = s[low];
        s[low++] = s[up];
        s[up--] = tmp;
    }
    return s;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
