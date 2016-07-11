---
layout: leetcode
date: 2016-07-11
title: Recover Binary Search Tree
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Two elements of a binary search tree (BST) are swapped by mistake.
>
>Recover the tree without changing its structure.
>
>**Note:**
>
>A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
>

***

## Solution

**Result:** Accepted **Time:** 48 ms

Here should be some explanations.

```cpp
class Solution {
public:
    void inorder(TreeNode * root,TreeNode * data[],int &ptr,int &last)
    {
        if(root == NULL) return ;
        inorder(root->left,data,ptr,last);
        if(last > root->val)
            ptr++;
        if(ptr == 0)
            data[ptr] = root;
        else if(data[0]->val > root->val)
        {
            if(ptr >= 2 && data[1]->val > root->val)
                data[1] = root;
            if(ptr == 1)
                data[ptr] = root;
        }
        last = root->val;
        inorder(root->right,data,ptr,last);
    }

    void recoverTree(TreeNode* root) {
        TreeNode * data[2]={0};
        int last = INT_MIN,ptr = 0;
        inorder(root,data,ptr,last);
        if(data[1])
            swap(data[0]->val,data[1]->val);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
