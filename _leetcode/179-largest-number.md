---
layout: leetcode
date: 2016-07-16
title: Largest Number
tags: [Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a list of non negative integers, arrange them such that they form the largest number.

For example, given `[3, 30, 34, 5, 9]`, the largest formed number is `9534330`.

**Note:** The result may be very large, so you need to return a string instead of an integer.


***

## Solution

**Result:** Accepted **Time:** 48 ms

Here should be some explanations.

```python
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self,nums):
        ret = ''.join(sorted([ str(x) for x in nums],cmp=lambda x,y:cmp(y+x,x+y)))
        return ret if ret[0] !='0' else "0"

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
