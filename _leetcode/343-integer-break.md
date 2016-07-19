---
layout: leetcode
date: 2016-07-18
title: Integer Break
tags: [Math, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a positive integer n, break it into the sum of **at least** two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

**Note:** You may assume that n is not less than 2 and not larger than 58.

**Hint:**

1. There is a simple O(n) solution to this problem.
2. You may check the breaking results of n ranging from 7 to 10 to discover the regularities.




***

## Solution

**Result:** Accepted **Time:**  0 ms

Here should be some explanations.

```c
int pow3[30]={1,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907,43046721,129140163,387420489,1162261467,};
int integerBreak(int n) {
    int rest[]={3,4,6};
    if( n < 4)
        return n==3?2:1;
    return pow3[n/3 -1]*rest[n%3];
}
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
