---
layout: leetcode
date: 2016-06-28
title: Permutation Sequence
tags: [Backtracking, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> The set `[1,2,3,…,n]` contains a total of $$n!$$ unique permutations.
>
>By listing and labeling all of the permutations in order,
>We get the following sequence (ie, for $$n = 3$$):
>
>  1. `"123"`
>  2. `"132"`
>  3. `"213"`
>  4. `"231"`
>  5. `"312"`
>  6. `"321"`
>
> Given $$n$$ and $$k$$, return the $$k^{th}$$ permutation sequence.
>
>**Note:** Given n will be between 1 and 9 inclusive.
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        string res;
        string nums = "123456789";
        int f[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880},i,j;
        for (i = n,--k; i >= 1; --i) {
            j = k / f[i - 1];
            k %= f[i - 1];
            res.push_back(nums[j]);
            nums.erase(nums.begin() + j);
        }
        return res;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
