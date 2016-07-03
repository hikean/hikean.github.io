---
layout: leetcode
date: 2016-06-24
title: Median of Two Sorted Arrays
tags: [Array, Divide and Conquer, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>There are two sorted arrays nums1 and nums2 of size m and n respectively.
>Find the median of the two sorted arrays. The overall run time complexity should be $$O(log (m+n))$$.
>
> **Example 1:**
>
>     nums1 = [1, 3]
>     nums2 = [2]
>     
>     The median is 2.0
>
>**Example 2:**
>
>     nums1 = [1, 2]
>     nums2 = [3, 4]
>      
>     The median is (2 + 3)/2 = 2.5


***

## Solution

**Result:** Accepted **Time:** 24ms

```c
int imin(int a, int b)
{
    return a > b ? b : a;
}

int find_kth(int* a, int na, int* b, int nb,int k)
{
    if(na < nb)
        return find_kth(b,nb,a,na,k);
    if(nb == 0)
        return a[k-1];
    if(k == 1)
        return imin(a[0],b[0]);
    int pb = imin(k / 2, nb), pa = k - pb;
    if(a[pa - 1] == b[pb - 1])
        return a[pa - 1];
    else if(a[pa - 1] > b[pb - 1])
        return find_kth(a,na,b+pb,nb - pb,k - pb);
    else
        return find_kth(a+pa,na-pa,b,na,k-pa);
}

double findMedianSortedArrays(int* a, int na, int* b, int nb) {
    const int cnt = na + nb;
    if(cnt & 1)
        return find_kth(a,na,b,nb,(cnt+1)/2);
    return (find_kth(a,na,b,nb,cnt/2) + find_kth(a,na,b,nb,cnt/2+1))*0.5;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(m+n)$$
- Space Complexity: $$O(1)$$
