---
layout: leetcode
date: 2016-07-13
title: Candy
tags: [Greedy]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> There are N children standing in a line. Each child is assigned a rating value.
>
>You are giving candies to these children subjected to the following requirements:
>
>  -  Each child must have at least one candy.
>  -  Children with a higher rating get more candies than their neighbors.
>
> What is the minimum candies you must give?
>     

***

## Solution

**Result:** Accepted **Time:** 40 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int candy(vector<int>& ratings) {
        if(!ratings.size())
            return 0;
        vector<int> candy(ratings.size(),1);
        for(int i=1;i<candy.size();i++)
            if(ratings[i]>ratings[i-1]&&candy[i]<=candy[i-1])
                candy[i]=candy[i-1]+1;
        for(int i=candy.size()-2;i>=0;i--)
            if(ratings[i]>ratings[i+1]&& candy[i]<=candy[i+1])
                candy[i]=candy[i+1]+1;
        return accumulate(begin(candy), end(candy), 0);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
