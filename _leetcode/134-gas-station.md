---
layout: leetcode
date: 2016-07-13
title: Gas Station
tags: [Greedy]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> There are N gas stations along a circular route, where the amount of gas at station i is `gas[i]`.
>
>You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
>
>Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
>
>**Note:**
>
>The solution is guaranteed to be unique.
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
int canCompleteCircuit(int* gas, int gsz, int* cost, int csz) {
    for(int start = 0; start < csz;start++)
    {
        int tank =  gas[start]  - cost[start],now = (start + 1)%gsz,stop = start;
        while(tank >= 0 && now != stop)
        {
            tank += gas[now]  - cost[now];
            now++,start++;
            now %= gsz;
        }
        if(tank >= 0 && now == stop)
            return stop;
        if(stop!= start) start--;
    }
    return -1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
