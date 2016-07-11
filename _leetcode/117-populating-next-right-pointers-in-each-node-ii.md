---
layout: leetcode
date: 2016-07-11
title: Populating Next Right Pointers in Each Node II
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Follow up for problem "Populating Next Right Pointers in Each Node".
>
>What if the given tree could be any binary tree? Would your previous solution still work?
>
>**Note:**
>
>You may only use constant extra space.
>For example,
>Given the following binary tree,
>
>              1
>            /  \
>           2    3
>          / \    \
>         4   5    7
>
> After calling your function, the tree should look like:
>
>              1 -> NULL
>            /  \
>           2 -> 3 -> NULL
>          / \    \
>         4-> 5 -> 7 -> NULL
>
>     

***

## Solution

**Result:** Accepted **Time:** 8 ms

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
