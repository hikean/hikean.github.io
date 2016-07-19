---
layout: leetcode
date: 2016-07-16
title: Binary Tree Right Side View
tags: [Tree, Depth First Search, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:

 Given the following binary tree,

<pre>
         1            <---
       /   \
      2     3         <---
       \     \
        5     4       <---
</pre>        

 You should return `[1, 3, 4]`.



***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void dfs(int depth,TreeNode * root,vector<int> &vec)
    {
        if(root == NULL) return;
        if(vec.size() <=  depth)
            vec.push_back(root->val);
        dfs(depth+1,root->right,vec);
        dfs(depth+1,root->left,vec);
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> vec;
        dfs(0,root,vec);
        return vec;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
