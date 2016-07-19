---
layout: leetcode
date: 2016-07-17
title: Burst Balloons
tags: [Divide and Conquer, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given `n` balloons, indexed from `0` to `n-1`. Each balloon is painted with a number on it represented by array `nums`. You are asked to burst all the balloons. If the you burst balloon `i` you will get `nums[left] * nums[i] * nums[right]` coins. Here `left` and `right` are adjacent indices of `i`. After the burst, the `left` and `right` then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

**Note:**

1. You may imagine `nums[-1] = nums[n] = 1`. They are not real therefore you can not burst them.
2. 0 ≤ `n` ≤ 500, 0 ≤ `nums[i]` ≤ 100

**Example:**

Given `[3, 1, 5, 8]`

Return `167`

<pre>
    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
</pre>



***

## Solution

**Result:** Accepted **Time:**  12 ms

Here should be some explanations.

```c
#define MAXN 256
int dp[MAXN][MAXN]={0},num[MAXN];
int max(int a,int b){return a > b? a:b;}
int maxCoins(int* nums, int nsz) {
    for(int i = 0 ; i < nsz; i++ )
        num[i+1] = nums[i];
    num[0] = num[nsz+1] = 1;
    for(int i = 0; i <= nsz; i++)
        for(int j = 1,k=i+j; k<= nsz;j++,k++)
        {
            dp[j][k] = 0;
            for(int t = j; t <= k; t++)
                dp[j][k] = max(dp[j][k],dp[j][t-1]+dp[t+1][k]+num[j-1]*num[t]*num[k+1]);
        }
    return dp[1][nsz];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n^2)$$
