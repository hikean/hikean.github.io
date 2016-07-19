---
layout: leetcode
date: 2016-07-18
title: Counting Bits
tags: [Dynamic Programming, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example:**

For `num = 5` you should return `[0,1,1,2,1,2]`.

**Follow up:**

- It is very easy to come up with a solution with run time **O(n*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
- Space complexity should be **O(n)**.
- Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.

**Hint:**

1. You should make use of what you have produced already.
2. Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
3. Or does the odd/even status of the number help you in calculating the number of 1s?




***

## Solution

**Result:** Accepted **Time:**  40 ms

Here should be some explanations.

```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    int * ary = malloc((num+2)*sizeof(int));
    *returnSize = num + 1;
    int ptr = 1;
    int cnt = 2;
    ary[0] = 0;
    ary[1] = 1;
    int limit = num / 2;
    while(ptr <= limit)
    {
        ary[(ptr<<1)] = ary[ptr];
        ary[(ptr<<1)|1] = ary[ptr]+1;
        ptr++;
    }
    return ary;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
