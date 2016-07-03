---
layout: leetcode
date: 2016-06-28
title: Largest Rectangle in Histogram
tags: [Array, Stack]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
> ![Histogram]({{site.baseurl}}/images/leetcode/84-histogram.png)
>Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.
> ![Histogram]({{site.baseurl}}/images/leetcode/84-histogram-area.png)
> The largest rectangle is shown in the shaded area, which has area = 10 unit.
>
>For example,
>
>Given heights = `[2,1,5,6,2,3]`,
>return `10`.
>

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int stck[65535];
int largestRectangleArea(int* hgt, int hgtsz) {
    int top = 0,ret = 0;
    for(int i = 0; i <= hgtsz; i ++)
    {
        int now = (i == hgtsz) ? 0:hgt[i];
        while(top && now < hgt[stck[top-1]])
        {
            int h = hgt[stck[--top]];
            int width = (top?i-1 - stck[top-1] : i);
            int tmp = h*width;
            if(tmp > ret)
                ret  = tmp;
        }
        stck[top++] = i;
    }
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
