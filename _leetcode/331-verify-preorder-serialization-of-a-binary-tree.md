---
layout: leetcode
date: 2016-07-18
title: Verify Preorder Serialization of a Binary Tree
tags: [Tree, Stack]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as `#`.

<pre>
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
</pre>

For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `#` represents a `null` node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character `'#'` representing `null` pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as `"1,,3"`.

**Example 1:**

`"9,3,4,#,#,1,#,#,2,#,6,#,#"`

Return `true`

**Example 2:**

`"1,#"`

Return `false`

**Example 3:**

`"9,#,#,1"`

Return `false`


***

## Solution

**Result:** Accepted **Time:**  0 ms

Here should be some explanations.

```c
int ptr;
bool valid(char * pre)
{
    if(pre[ptr] == ',') ptr++;
    if(pre[ptr] == '\0')
        return false;
    if(pre[ptr++] =='#')
        return true;
    while(isdigit(pre[ptr])) ptr++;
    return valid(pre) && valid(pre);
}

bool isValidSerialization(char* preorder) {
    ptr = 0;
    return valid(preorder) && preorder[ptr] == '\0';
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
