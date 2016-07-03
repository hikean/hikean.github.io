---
layout: leetcode
date: 2016-06-23
title: Roman to Integer
tags: [String, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a roman numeral, convert it to an integer.
>
> Input is guaranteed to be within the range from 1 to 3999.
>   

***

## Solution

**Result:** Accepted **Time:** 24ms

Here should be some explanations.

```c
int romanToInt(char* str) {
    int table[256] = {0};
    const char keys[]="IVXLCDM";
    const int values[]={1,5,10,50,100,500,1000};
    for(int i = 0; i < sizeof(keys); i++)
        table[keys[i]] = table[keys[i] | 32] = values[i];
    int ans = 0, last = 0, now = 0;
    while(*str)
    {
        now = table[*(str++)];
        ans += now;
        if(last < now)
            ans -= (last << 1);
        last = now;
    }
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
