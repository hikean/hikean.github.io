---
layout: leetcode
date: 2016-07-11
title: Populating Next Right Pointers in Each Node
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a binary tree
>     
>         struct TreeLinkNode {
>           TreeLinkNode *left;
>           TreeLinkNode *right;
>           TreeLinkNode *next;
>         }
>
>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
>
>Initially, all next pointers are set to NULL.
>
>Note:
>
>You may only use constant extra space.
>
>You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
>
>For example,
>
>Given the following perfect binary tree,
>
>              1
>            /  \
>           2    3
>          / \  / \
>         4  5  6  7
>
>After calling your function, the tree should look like:
>
>              1 -> NULL
>            /  \
>           2 -> 3 -> NULL
>          / \  / \
>         4->5->6->7 -> NULL
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
struct TreeLinkNode * stck[1024];
void dfs(struct TreeLinkNode * root ,int depth)
{
    if(root == NULL) return ;
    root->next = NULL;
    if(stck[depth])
        stck[depth]->next = root;
    stck[depth] = root;
    dfs(root->left,depth + 1);
    dfs(root->right,depth + 1);
}
void connect(struct TreeLinkNode *root) {
    memset(stck,0,sizeof(stck));
    dfs(root,0);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
