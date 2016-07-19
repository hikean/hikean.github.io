---
layout: leetcode
date: 2016-07-11
title: Best Time to Buy and Sell Stock III
tags: [Array, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Say you have an array for which the $$i^{th}$$ element is the price of a given stock on day i.
>
>Design an algorithm to find the maximum profit. You may complete at most two transactions.
>
>**Note:**
>
>You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
>
>    

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int imax(int a, int b){ return a > b ? a : b; }

int maxProfit(int* prices, int psz)
{
    // 0 one buy 1 one sell 2 two buy 3 tow sell
    int dp[2][4]={-prices[0], 0, INT_MIN ,0}, now = 1, last = 0;
    for(int i = 1; i < psz; i++)
    {
        dp[now][0] = imax(dp[last][0], -prices[i] );
        dp[now][1] = imax(dp[last][1], dp[last][0] + prices[i]);
        dp[now][2] = imax(dp[last][2], dp[last][1] - prices[i]);
        dp[now][3] = imax(dp[last][3], dp[last][2] + prices[i]);
        last = now;
        now ^= 1;
    }
    return imax(dp[!(psz&1)][3],dp[!(psz&1)][1]);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
