---
layout: leetcode
date: 2016-06-23
title: ZigZag Conversion
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
>     
>     P   A   H   N
>     A P L S I I G
>     Y   I   R
>
> And then read line by line: `"PAHNAPLSIIGYIR"`
>     
> Write the code that will take a string and make this conversion given a number of rows:
>
>      string convert(string text, int nRows);
>
> `convert("PAYPALISHIRING", 3)` should return `"PAHNAPLSIIGYIR"`.


***

## Solution

**Result:** Accepted **Time:** 8ms

It's easy to solve.

```c
char* convert(char* s, int numRows) {
    int len = strlen(s);
    int i,idx,cnt=0,da,db;
    if(numRows < 2)
        return s;
    char * str = malloc(sizeof(char) * (len + 5));
    for(i = 1; i <= numRows ; i++)
    {
        idx = i-1;
        str[cnt++] = s[idx ];
        da = 2*(numRows - i);
        db = 2*(i-1);
        while(idx < len)
        {
            idx += da;
            if(i!= numRows && idx < len)
                str[cnt++] = s[idx ];
            idx += db;
            if( i!=1 && idx < len)
                str[cnt++] = s[idx];
        }
    }
    str[cnt] = 0;
    return str;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
