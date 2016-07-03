---
layout: leetcode
date: 2016-06-26
title: Jump Game II
tags: [Array, Greedy]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array of non-negative integers, you are initially positioned at the first index of the array.
>
> Each element in the array represents your maximum jump length at that position.
>
> Your goal is to reach the last index in the minimum number of jumps.
>
>For example:
>
> Given array A = `[2,3,1,1,4]`
>
> The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
>
> **Note:**
>
>You can assume that you can always reach the last index.
>    

***

## Solution

**Result:** Accepted **Time:** 8ms

Here should be some explanations.

```c
int jump(int* nums, int numsSize) {
    int now = 0,ret = 0,last = 0,i,t;
    for(i = 0,t = nums[0],--numsSize; now < numsSize; t = ++i + nums[i]){
        if(t > now) now = t;
        if(i == last) ++ret,last = now;
    }
    return (now > last)? ret + 1 : ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
