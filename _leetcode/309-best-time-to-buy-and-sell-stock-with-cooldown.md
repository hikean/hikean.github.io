---
layout: leetcode
date: 2016-07-17
title: Best Time to Buy and Sell Stock with Cooldown
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

**Example:**

<pre>
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
</pre>


***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy[2] ={INT_MIN,INT_MIN},sell[2]={0},cool[2]={0};
        for (int i = 0; i < prices.size(); i++) {
            int today = i&1, yesterday = (i&1)^1;
            buy[today] = max(buy[yesterday], cool[yesterday] - prices[i]);
            sell[today] = buy[yesterday] + prices[i];
            cool[today] = max(cool[yesterday], sell[yesterday]);
        }
        return max(max(sell[0],sell[1]),max(cool[0],cool[1]));
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$



```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int frozen = 1 + 1;
        int k = (prices.size() + 1)/(frozen + 1) + 2, days = frozen + 3;
        vector<vector<long long>> buy(k, vector<long long>(days, INT_MIN));
        vector<vector<long long>> sell(k, vector<long long>(days, 0));
        for(int i = 1; i <= prices.size(); i ++){
            for(int j = k -1; j > 0; j--){
                buy[j][i%days] = max(sell[j-1][(i-frozen + days) %days]-prices[i-1], buy[j][(i-1)%days]);
                sell[j][i%days] = max(buy[j][(i-1)%days] + prices[i-1], sell[j][(i-1)%days]);
            }
        }
        long long ret = 0;
        for(int i = 1;i < k; i++)
            ret = max(ret, sell[i][prices.size()%days]);
        return ret;
    }
};
```
