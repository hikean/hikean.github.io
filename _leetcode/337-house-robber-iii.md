---
layout: leetcode
date: 2016-07-18
title: House Robber III
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

**Example 1:**

<pre>     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1</font>
</pre>

Maximum amount of money the thief can rob = `3` + `3` + `1` = **7**.

**Example 2:**

<pre>     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1</font>
</pre>

Maximum amount of money the thief can rob = `4` + `5` = **9**.




***

## Solution

**Result:** Accepted **Time:**  15 ms

Here should be some explanations.

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 struct State{
     int a,b;
     int get_max()
     {
         return a > b ? a : b;
     }
     State():a(0),b(0){}
     State(int aa,int bb):a(aa),b(bb){}
 };
 
State robber(TreeNode * root)
{
    if(root == NULL)
        return State();
    State left = robber(root->left);
    State right = robber(root->right);
    return State(left.get_max() + right.get_max(), left.a + right.a + root->val);
}
class Solution {
public:
    int rob(TreeNode* root) {
        return robber(root).get_max();
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
