---
layout: leetcode
date: 2016-06-25
title: Integer to Roman
tags: [String, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an integer, convert it to a roman numeral.
>
> Input is guaranteed to be within the range from 1 to 3999.
>

***

## Solution

**Result:** Accepted **Time:** 24ms

Here should be some explanations.

```c
char* intToRoman(int n) {
    const int num[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char chrs[][3] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int idx = 0, i = 0;
    char * str = malloc(sizeof(char) * 32);
    while(n)
    {
        while(n < num[i]) i++;
        n -= num[i];
        str[idx++] = chrs[i][0];
        if(i & 1)
            str[idx++] = chrs[i][1];
    }
    str[idx] = 0;
    return str;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(log(n))$$
