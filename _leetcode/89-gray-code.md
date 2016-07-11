---
layout: leetcode
date: 2016-07-07
title: Gray Code
tags: [Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> The gray code is a binary numeral system where two successive values differ in only one bit.
>
>Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
>
>For example, given `n = 2`, return `[0,1,3,2]`. Its gray code sequence is:
>
>     00 - 0
>     01 - 1
>     11 - 3
>     10 - 2
>
>**Note:**
>
>For a given n, a gray code sequence is not uniquely defined.
>
>For example, `[0,2,3,1]` is also a valid gray code sequence according to the above definition.
>
>For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.



***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* grayCode(int n, int* returnSize) {
    int * ans = malloc(sizeof(int) * (1<<n));
    *returnSize = 1 << n;
    for(int i = 0; i < (1<<n); i++)
        ans[i] = 0;
    for(int i = 0; i < n; i++)
    {  
        int t = 0;
        int bit = 1 << i;
        for(int j = 0 ; j < (1<<n); j+=bit)
        {

            if(t == 1 || t == 2)
                for(int k = 0; k < bit; k++)
                    ans[j + k] |= bit;
            t++;
            t &= 3;
        }
    }
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n*log(n))$$
- Space Complexity: $$O(n)$$
