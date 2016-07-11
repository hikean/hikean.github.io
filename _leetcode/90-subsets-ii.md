---
layout: leetcode
date: 2016-07-07
title: Subsets II
tags: [Array, Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a collection of integers that might contain duplicates, nums, return all possible subsets.
>
>**Note:** The solution set must not contain duplicate subsets.
>
>For example,
>
> If **nums** = `[1,2,2]`, a solution is:
>
>     [
>       [2],
>       [1],
>       [1,2,2],
>       [2,2],
>       [1,2],
>       []
>     ]
>     

***

## Solution

**Result:** Accepted **Time:** 12 ms

Here should be some explanations.

```cpp
class Solution {
public:
      int index[32];
      int digit[32];
      int frequent[32];
    bool next(int cnt)
    {
        for(int i = 0; i < cnt; i++)
            if(frequent[index[i]] > 1)
            {
                if(digit[i] > 1)
                {
                    digit[i] --;
                    return true;
                }
                else
                    digit[i] = frequent[index[i]];
            }
        return false;
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int> > ans;
        int cnt = 1, ilast = 0;
        for(int i = 1, len = nums.size(); i  < len; i ++)
            if(nums[i] != nums[i-1])
            {
                frequent[cnt - 1] = i - ilast;
                //frequent.push_back(i - ilast);
                nums[cnt++] = nums[i];
                ilast = i;
            }
        //frequent.push_back(nums.size() - ilast);
        frequent[cnt-1] = nums.size() - ilast;
        const int limit = 1 << cnt;
        for(int i = 0; i < limit; i++)
        {
            int j = 0;
            int tmp = i;
            int set_len = 0;
            while(tmp)
            {
                if(tmp&1)
                {
                    digit[set_len] = frequent[j];
                    index[set_len++] = j;
                }
                tmp >>= 1;  
                j++;
            }
            do{
                vector<int> st;
                for(int a = 0; a < set_len; a++)
                    for(int b = 0; b < digit[a]; b++)
                        st.push_back(nums[index[a]]);
                ans.push_back(st);
            }while(next(set_len));
        }
        return ans;

    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n!)$$
- Space Complexity: $$O(n!)$$
