---
layout: leetcode
date: 2016-06-26
title: Count and Say
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> The count-and-say sequence is the sequence of integers beginning as follows:
>
>`1, 11, 21, 1211, 111221, ...``
>
>`1` is read off as `"one 1"` or `11`.
>
>`11` is read off as `"two 1s"` or `21`.
>
>`21` is read off as `"one 2"`, then `"one 1"` or `1211`.
>
>Given an integer $$n$$, generate the $$n^{th}$$ sequence.
>
>**Note:** The sequence of integers will be represented as a string.
>
>     

***

## Solution

**Result:** Accepted **Time:** 12ms

Here should be some explanations.

```cpp

vector<string> say;
char buffer[1024 * 256];
char buf[1024*256];
int cnt=0;
class Solution {
public:
    Solution(){
        if(cnt) return;
        say.push_back("1");cnt = 1;

    }
    string countAndSay(int n) {
       return get_nth(n);
    }
    string get_nth(int n)
    {
        if(n < cnt)
            return say[n];
        const char* tmp = say[cnt-1].c_str();
        char cur = tmp[0];
        int len = say[cnt-1].size();
        int num = 0;
        int idx = 0;
        buf[0] = 0;
        while(cnt < n)
        {
            while(idx <= len)
            {
                if(cur == tmp[idx++])
                    num++;
                else
                {
                    sprintf(buffer,"%s%d%c",buf,num,cur);
                    strcpy(buf,buffer);
                    cur = tmp[idx-1];
                    num = 1;
                }
            }
            say.push_back(string(buffer));
            tmp = say[cnt++].c_str();
            buf[0]=0;
            cur = tmp[0];
            idx = 0;
            num = 0;
            len = say[cnt -1].size();
        }
        return say[n-1];
    }

};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
