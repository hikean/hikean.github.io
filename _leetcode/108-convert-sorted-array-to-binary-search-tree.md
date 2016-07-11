---
layout: leetcode
date: 2016-07-11
title: Convert Sorted Array to Binary Search Tree
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
>

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
struct TreeNode * buildtree(int *nums,int low,int up)
{
    if(low >= up)
        return NULL;
    struct TreeNode * tmp = malloc(sizeof(struct TreeNode));
    int mid = low + ((up - low) >> 1);
    tmp->val = nums[mid];
    tmp->left = buildtree(nums,low,mid);
    tmp->right = buildtree(nums,mid+1,up);
    return tmp;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return buildtree(nums,0,numsSize);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
