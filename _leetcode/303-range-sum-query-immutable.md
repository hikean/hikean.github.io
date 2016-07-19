---
layout: leetcode
date: 2016-07-17
title: Range Sum Query Immutable
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an integer array *nums*, find the sum of the elements between indices *i* and *j (i ≤ j)*, inclusive.

**Example:**

<pre>
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
</pre>

**Note:**

1. You may assume that the array does not change.
2. There are many calls to sumRange function.



***

## Solution

**Result:** Accepted **Time:**  576 ms

Here should be some explanations.

```c
struct NumArray {
    int * ary;
    int cnt;
    
};

/** Initialize your data structure here. */
struct NumArray* NumArrayCreate(int* nums, int numsSize) {
    struct NumArray * numAry = (struct NumArray *)malloc(sizeof(struct NumArray));
    int * ptr = (int * ) malloc((numsSize + 5)*sizeof(int));
    numAry->ary = ptr;
    numAry->cnt = numsSize;
    *ptr = 0;
    int sum = 0;
    while(numsSize--)
        {
            sum += *(nums++);
            *(++ptr) = sum;
        }
    return numAry;
}

int sumRange(struct NumArray* numArray, int i, int j) {
    
    return numArray->ary[j+1] - numArray->ary[i];
}

/** Deallocates memory previously allocated for the data structure. */
void NumArrayFree(struct NumArray* numArray) {
    //free(numArray->ary);
    //free(numArray);
    
}

// Your NumArray object will be instantiated and called as such:
// struct NumArray* numArray = NumArrayCreate(nums, numsSize);
// sumRange(numArray, 0, 1);
// sumRange(numArray, 1, 2);
// NumArrayFree(numArray);
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
