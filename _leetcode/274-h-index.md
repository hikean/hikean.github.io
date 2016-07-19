---
layout: leetcode
date: 2016-07-17
title: H-Index
tags: [Hash Table, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): "A scientist has index h if h of his/her N papers have **at least** h citations each, and the other N − h papers have no more than h citations each."

For example, given `citations = [3, 0, 6, 1, 5]`, which means the researcher has `5` papers in total and each of them had received `3, 0, 6, 1, 5` citations respectively. Since the researcher has `3` papers with **at least** `3` citations each and the remaining two with no more than 3 citations each, his h-index is `3`.

**Note:** If there are several possible values for `h`, the maximum one is taken as the h-index.

**Hint:**

1. An easy approach is to sort the array first.
2. What are the possible values of h-index?
3. A faster approach is to use extra space.





***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
class Solution {
public:
    int hIndex(vector<int>& cit) {
        if(cit.size() < 1) return 0;
        sort(cit.begin(),cit.end());
        reverse(cit.begin(),cit.end());
        int i;
        for( i = 0; i < cit.size() && cit[i] > i; i++);
        return i;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(1)$$
