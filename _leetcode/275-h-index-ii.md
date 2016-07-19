---
layout: leetcode
date: 2016-07-17
title: H-Index II
tags: [Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

**Follow up** for [H-Index](https://leetcode.com/problems/h-index/): What if the `citations` array is sorted in ascending order? Could you optimize your algorithm?

**Hint:**

1. Expected runtime complexity is in $$O( \log n)$$ and the input is sorted.



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
int hIndex(int* cit, int len) {
    int step = len - 1, low = 0;
    while(step > 0)
    {
        while(low + step > len || ( step && cit[len - low -1 - step] <= low + step))
            step >>= 1;
        low += step;
    }
    if(!len || cit[len-1] < 1)
        return 0;
    return low+1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
