---
layout: leetcode
date: 2016-07-18
title: Coin Change
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

You are given coins of different denominations and a total *amount* of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

**Example 1:**

coins = `[1, 2, 5]`, amount = `11`

return `3` (11 = 5 + 5 + 1)

**Example 2:**

coins = `[2]`, amount = `3`

return `-1`.

**Note:**

You may assume that you have an infinite number of each kind of coin.



***

## Solution

**Result:** Accepted **Time:**  20 ms

Here should be some explanations.

```c
#define MAXN 65535  
int dp[MAXN];  
int coinChange(int* coins, int coinsSize, int amount) {
    memset(dp,0x3f,sizeof(int)*(amount+1));
    dp[0] = 0;
    for(int i = 0; i < coinsSize; i++)
        for(int j = 0,k = coins[i]; j <= amount; j++,k++)
            dp[k] = dp[j] + 1 < dp[k] ? dp[j]+1 : dp[k];
    return dp[amount] == 0x3f3f3f3f? -1:dp[amount];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
