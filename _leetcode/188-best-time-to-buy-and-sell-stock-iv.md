---
layout: leetcode
date: 2016-07-16
title: Best Time to Buy and Sell Stock IV
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

**Note:**

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int imax(int a, int b){ return a > b ? a : b; }

int dp[2][10240][2];
int maxProfit(int k, int* prices, int psz) {
    memset(dp,0,sizeof(dp));
    dp[0][0][0] = -prices[0];
    int now = 1, last = 0, ret = 0;
    if(k > psz/2 )
    {
        int ret = 0;
    	for(int i = 1; i < psz; i++)
    		if (prices[i] > prices[i-1])
    			ret += prices[i] - prices[i-1];
    	return ret;
    }
    for(int i = 1; i < k; i++)
        dp[0][i][0] = dp[1][i][0] = INT_MIN;
    for(int i = 1; i < psz; i++)
    {
        dp[now][0][0] = imax(dp[last][0][0], -prices[i] );
        dp[now][0][1] = imax(dp[last][0][1], dp[last][0][0] + prices[i]);
        for(int j = 1; j < k; j++)
        {
            int tmp = dp[last][j-1][1] - prices[i];
            dp[now][j][0] = dp[last][j][0] > tmp ?  dp[last][j][0] : tmp;
            tmp = dp[last][j][0] + prices[i];
            dp[now][j][1] = dp[last][j][1] > tmp? dp[last][j][1] : tmp;
        }
        last = now;
        now ^= 1;
    }
    for(int i = 0; i < k; i++)
        ret = imax(imax(dp[0][i][1],dp[1][i][1]),ret);
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(kn)$$
- Space Complexity: $$O(k)$$
