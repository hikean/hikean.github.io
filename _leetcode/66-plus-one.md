---
layout: leetcode
date: 2016-06-28
title: Plus One
tags: [Array, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a non-negative number represented as an array of digits, plus one to the number.
>
>The digits are stored such that the most significant digit is at the head of the list.
>
>

***

## Solution

**Result:** Accepted **Time:** x ms

Here should be some explanations.

```c
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int carry = 1;
    int len = 0,tmp;
    int * ans = malloc(sizeof(int)*(digitsSize+4));
    int * ary = malloc(sizeof(int)*(digitsSize+4));
    for(tmp = 0; tmp < digitsSize;tmp++)
        ans[tmp] = digits[digitsSize-tmp -1];

    while(carry || len < digitsSize)
    {
        tmp = (carry + ans[len]);
        carry = tmp/10;
        ary[len++] = tmp%10;
    }
    for(tmp = 0; tmp < len;tmp++)
        ans[tmp] = ary[len-tmp -1];
    free(ary);
    *returnSize = len;
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
