---
layout: leetcode
date: 2016-07-16
title: Excel Sheet Column Number
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Related to question [Excel Sheet Column Title](/leetcode/168-excel-sheet-column-title/)

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

<pre>
         A -> 1
         B -> 2
         C -> 3
         ...
         Z -> 26
         AA -> 27
         AB -> 28
</pre>     


***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int titleToNumber(char* s) {
    int ret = 0;
    while(*s)
        ret = ret * 26 + *(s++) - 'A' + 1;
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
