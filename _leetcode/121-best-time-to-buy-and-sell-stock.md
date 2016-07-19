---
layout: leetcode
date: 2016-07-11
title: Best Time to Buy and Sell Stock
tags: [Array, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Say you have an array for which the ith element is the price of a given stock on day i.
>
>If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
>
>**Example 1:**
>
>     Input: [7, 1, 5, 3, 6, 4]
>     Output: 5
>     
>     max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
>
>**Example 2:**
>
>     Input: [7, 6, 4, 3, 1]
>     Output: 0
>     
>     In this case, no transaction is done, i.e. max profit = 0.
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int maxProfit(int* prices, int psz) {
    int ret = 0;
    int buy = prices[0],sell=prices[0];
    for(int i = 0; i < psz; i++)
    {
        if(prices[i] <= buy)
            sell = buy = prices[i];
        if(prices[i] >= sell)
        {
            sell = prices[i];
            if(ret < sell - buy)
                ret = sell - buy;
        }
    }
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
