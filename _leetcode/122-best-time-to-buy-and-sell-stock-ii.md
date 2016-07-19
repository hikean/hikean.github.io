---
layout: leetcode
date: 2016-07-11
title: Best Time to Buy and Sell Stock II
tags: [Array, Greedy]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Say you have an array for which the $$i^{th}$$ element is the price of a given stock on day i.
>
>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
>
>   

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int maxProfit(int* prices, int pricesSize) {
    int mini, maxi;
    int cnt = 0, ans = 0;
    mini = maxi = prices[0];
    while(cnt < pricesSize)
    {
        while(++cnt < pricesSize && prices[cnt] >= maxi)
            maxi = prices[cnt];
        ans += maxi - mini;
        maxi = mini = prices[cnt];
    }
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
