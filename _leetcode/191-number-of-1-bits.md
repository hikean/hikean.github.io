---
layout: leetcode
date: 2016-07-16
title: Number of 1 Bits
tags: [Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation `00000000000000000000000000001011`, so the function should return 3.

     

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int sum = 0;
        while(n)
        {
            sum += n&1;
            n>>=1;
        }
        return sum;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
