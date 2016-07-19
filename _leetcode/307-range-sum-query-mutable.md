---
layout: leetcode
date: 2016-07-17
title: Range Sum Query - Mutable
tags: [Segment Tree, Binary Index Tree]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


Given an integer array nums, find the sum of the elements between indices *i* and *j (i ≤ j)*, inclusive.

The *update(i, val)* function modifies *nums* by updating the element at index i to val.

**Example:**

<pre>
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
</pre>

**Note:**

1. The array is only modifiable by the *update* function.
2. You may assume the number of calls to *update* and *sumRange* function is distributed evenly.



***

## Solution

**Result:** Accepted **Time:**  20 ms

Here should be some explanations.

```c
struct NumArray {
    int size,* BIT;
};

int sum(int * bit,int x)
{
    int ret = 0;
    while(x)
    {
        ret += bit[x];
        x-= (x&-x);
    }
    return ret;
}
void update(struct NumArray* tmp, int i, int val) {
    i++;
    val -= sum(tmp->BIT,i) - sum(tmp->BIT,i-1);
    while(i <= tmp->size)
    {
        tmp->BIT[i] += val;
        i+= (i&-i);
    }
}
/** Initialize your data structure here. */
struct NumArray* NumArrayCreate(int* nums, int numsSize) {
    struct NumArray  *tmp = (struct NumArray  *)malloc(sizeof(struct NumArray));
    tmp->BIT = (int *)malloc(sizeof(int)*(numsSize+2));
    memset(tmp->BIT,0,sizeof(int)*(numsSize+2));
    tmp->size = numsSize;
    for(int i = 0; i < numsSize; i++)
        update(tmp,i,nums[i]);
    return tmp;
}

int sumRange(struct NumArray* numArray, int i, int j) {
    return sum(numArray->BIT,j+1) - sum(numArray->BIT,i);

}
/** Deallocates memory previously allocated for the data structure. */
void NumArrayFree(struct NumArray* numArray) {
    free(numArray->BIT);
    free(numArray);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
