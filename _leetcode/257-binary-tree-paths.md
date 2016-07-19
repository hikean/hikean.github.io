---
layout: leetcode
date: 2016-07-16
title: Binary Tree Paths
tags: [Tree, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

<pre>
   1
 /   \
2     3
 \
  5
</pre>

All root-to-leaf paths are:

<pre>
["1->2->5", "1->3"]
</pre>


***

## Solution

**Result:** Accepted **Time:** 4 ms

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
class Solution {
public:
    string get_string(int n)
    {
        char tmp[10];
        sprintf(tmp,"%d",n);
        return string(tmp);
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        TreeNode * now = NULL;
        string tmp = "";
        if(root == NULL)
            return ans;
        stack<string> str_stk;
        stack<TreeNode *> stk;
        if(root->right)
        {
            stk.push(root->right);
            str_stk.push(get_string(root->val));
        }
       if(root->left)
        {
            stk.push(root->left);
            str_stk.push(get_string(root->val));
        }
        if(root->left == NULL && root->right == NULL)
            ans.push_back(get_string(root->val));
        while(!stk.empty())
        {
            now = stk.top();stk.pop();
            tmp = str_stk.top();str_stk.pop();
            tmp = tmp + "->" + get_string(now->val);
            if(now->left == NULL && now->right == NULL)
                ans.push_back(tmp);
            else
            {
                if(now -> right != NULL)
                {
                    stk.push(now->right);
                    str_stk.push(tmp);
                }
                if(now -> left != NULL)
                {
                    stk.push(now->left);
                    str_stk.push(tmp);
                }
            }
        }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
