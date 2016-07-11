---
layout: leetcode
date: 2016-07-11
title: Maximum Depth of Binary Tree
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree, find its maximum depth.
>
>The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
>



***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
struct TreeNode * stack[1024],* tmp;
 int maxDepth(struct TreeNode * root)
 {
     int top = 0,ans = 0,val;
     struct TreeNode * left ,* right;
     if(root == NULL) return 0;
     stack[top++] = root;
     root->val = 1;
     while(top)
     {
         tmp = stack[--top];
         val = tmp->val;
         left = tmp ->left;
         right = tmp -> right;
         if(val > ans)
            ans = val;
         if(left)
         {
            stack[top++] = left;
            left->val = val+1;
         }
         if(right)
         {
            stack[top++] = right;
            right->val = val+1;
         }
     }
     return ans;
 }

int maxDepth2(struct TreeNode* root) {
    if(root == NULL ) return 0;
    int a = maxDepth(root->left);
    int b = maxDepth(root->right);
    return (a>b?a:b)+1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
