---
layout: leetcode
date: 2016-07-17
title: Ugly Number II
tags: [Dynamic Programming, Heap, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include `2, 3, 5`. For example, `1, 2, 3, 4, 5, 6, 8, 9, 10, 12` is the sequence of the first 10 ugly numbers.

Note that `1` is typically treated as an ugly number.

**Hint:**

1. The naive approach is to call `isUgly` for every number until you reach the $$n^{th}$$ one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
3. The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L<sub>1</sub>, L<sub>2</sub>, and L<sub>3</sub>.
4. Assume you have U<sub>k</sub>, the $$k^{th}$$ ugly number. Then U<sub>k+1</sub> must be Min(L<sub>1</sub> * 2, L<sub>2</sub> * 3, L<sub>3</sub> * 5).




***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
int data[2000]={0};

int nthUglyNumber(int n)
{

   if(!data[0])
   {
       int p2, p3, p5, v2, v3, v5, cnt, tmp;
       cnt = data[0] = 1;
       p2 = p3 = p5 = 0;
       while(cnt < 2000)
       {
           tmp = v2 = data[p2] * 2;
           v3 = data[p3] * 3;
           v5 = data[p5] * 5;
           if( tmp > v3 ) tmp = v3;
           if( tmp > v5 ) tmp = v5;
           p2 += v2 == tmp;
           p3 += v3 == tmp;
           p5 += v5 == tmp;
           data[cnt++] = tmp;
       }
   }
   return data[n - 1];
}

```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
