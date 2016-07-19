---
layout: leetcode
date: 2016-07-17
title: Bulb Switcher
tags: [Math, Brainteaser]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i<sup>th</sup> round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

**Example:**

<pre>
Given n = 3. 

At first, the three bulbs are <b>[off, off, off]</b>.
After first round, the three bulbs are <b>[on, on, on]</b>.
After second round, the three bulbs are <b>[on, off, on]</b>.
After third round, the three bulbs are <b>[on, off, off]</b>. 

So you should return <b>1</b>, because there is only one bulb is on.

</pre>

***

## Solution

**Result:** Accepted **Time:**  0 ms

Here should be some explanations.

```c
int bulbSwitch(int n) {
    return sqrt(n+0.5);
}
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
