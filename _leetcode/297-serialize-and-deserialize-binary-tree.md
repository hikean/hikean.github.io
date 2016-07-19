---
layout: leetcode
date: 2016-07-17
title: Serialize And Deserialize Binary Tree
tags: [Tree, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

<pre>
    1
   / \
  2   3
     / \
    4   5
</pre>

as ``"[1,2,3,null,null,4,5]"``, just the same as [how LeetCode OJ serializes a binary tree](https://leetcode.com/faq/#binary-tree). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

**Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.



***

## Solution

**Result:** Accepted **Time:**  16 ms

Here should be some explanations.

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/** Encodes a tree to a single string. */
char str[102400];
int ptr = 0;
void srlz(struct TreeNode * root)
{
    if(root == NULL)
    {
        str[ptr++] = '#';
        return ;
    }
    sprintf(str+ptr,"%d,",root->val);
    while(str[ptr]) ptr++;
    srlz(root->left);
    srlz(root->right);
}

char* serialize(struct TreeNode* root) {
    ptr = 0;
    srlz(root);
    str[ptr] = '\0';
    return str;
}

struct TreeNode * dsrlz(char * data)
{
    if(data[ptr] =='\0') return NULL;
    if(data[ptr] == ',') ptr++;
    if(data[ptr] == '#')
    {
        ptr++;
        return NULL;
    }
    int tmp = 0;
    int opt = 1;
    if(data[ptr] == '-') opt = -1,ptr++;
    while(isdigit(data[ptr])) tmp = tmp * 10 + opt*(data[ptr++] - '0');
    struct TreeNode * root = malloc(sizeof(struct TreeNode));
    root->val = tmp;
    root->left = dsrlz(data);
    root->right = dsrlz(data);
    return root;
}

/** Decodes your encoded data to tree. */
struct TreeNode* deserialize(char* data) {
    ptr = 0;
    return dsrlz(data);
}

// Your functions will be called as such:
// char* data = serialize(root);
// deserialize(data);
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
