---
layout: leetcode
date: 2016-07-11
title: Pascal's Triangle
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given numRows, generate the first numRows of Pascal's triangle.
>
>For example, given numRows = 5,
>
>Return
>
>     [
>          [1],
>         [1,1],
>        [1,2,1],
>       [1,3,3,1],
>      [1,4,6,4,1]
>     ]
>
>     

***

## Solution

**Result:** Accepted **Time:** 3 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans(numRows);
        if(numRows)
            ans[0].push_back(1);
        if(numRows > 1)
        {
            ans[1].push_back(1);
            ans[1].push_back(1);
            for(int i = 2 ;i < numRows;  i++)
            {
                ans[i] = vector<int>(i+1);
                ans[i][0] = 1;
                for(int j=1; j < i; j++)
                    ans[i][j]=ans[i-1][j-1] + ans[i-1][j];
                ans[i][i] = 1;
            }
        }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
