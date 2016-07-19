---
layout: leetcode
date: 2016-07-16
title: Happy Number
tags: [Hash Table, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.


**Example:** 19 is a happy number

$$1^2 + 9^2 = 8^2$$

$$8^2 + 2^2 = 68$$

$$6^2 + 8^2 = 100$$

$$1^2 + 0^2 + 0^2 = 1$$

***

## Solution

**Result:** Accepted **Time:** 52 ms

Here should be some explanations.

```python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st=set()
        while n not in st:
            sum = 0
            last  = n
            while n:
                tmp = n % 10;
                sum += tmp * tmp
                n /= 10
            st.add(last)
            n = sum
            if n == 1:
                return True
        return False

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
