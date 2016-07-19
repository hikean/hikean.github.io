---
layout: leetcode
date: 2016-07-16
title: Reverse Bits
tags: [Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as **00000010100101000001111010011100**), return 964176192 (represented in binary as **00111001011110000010100101000000**).

**Follow up:**

If this function is called many times, how would you optimize it?


***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans = 0;
        int i=32;
        while(i--)
        {
            ans = (ans << 1) | (n&1);
            n >>= 1;
        }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
