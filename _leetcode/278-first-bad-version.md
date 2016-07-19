---
layout: leetcode
date: 2016-07-17
title: First Bad Version
tags: [Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions ``[1, 2, ..., n]`` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which will return whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


***

## Solution

**Result:** Accepted **Time:**  0 ms

Here should be some explanations.

```c
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

int firstBadVersion(int n) {
    int st=1,ed=n;
    int mid = st + ((ed - st) >> 1);
    while (st < ed)
    {
        if(isBadVersion(mid))
            ed = mid -1;
        else
            st = mid + 1;
        mid = st + ((ed - st )>>1);
    }
    if(isBadVersion(mid))
        return mid;
    return mid + 1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
