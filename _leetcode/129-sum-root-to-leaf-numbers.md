---
layout: leetcode
date: 2016-07-13
title: Sum Root to Leaf Numbers
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
>
>An example is the root-to-leaf path 1->2->3 which represents the number 123.
>
>Find the total sum of all root-to-leaf numbers.
>
>For example,
>
>         1
>        / \
>       2   3
>
> The root-to-leaf path `1->2` represents the number `12`.
>
> The root-to-leaf path `1->3` represents the number `13`.
>
> Return the sum = 12 + 13 = `25`.
>
>

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
int sum_tree(struct TreeNode* root,int sum)
 {
     if(root == NULL) return 0;
     sum = sum *10 + root->val;
     int ret =  sum_tree(root->left,sum) + sum_tree(root->right,sum);
     return ret==0?sum:ret;
 }

int sumNumbers(struct TreeNode* root) {
    return sum_tree(root,0);
}

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
