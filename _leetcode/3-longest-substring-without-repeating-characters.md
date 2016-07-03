---
layout: leetcode
date: 2016-06-22
title: Longest Substring Without Repeating Characters
tags: [Hash Table, Two Pointers, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>Given a string, find the length of the longest substring without repeating characters.
>
>**Examples:**
>
>     Given "abcabcbb", the answer is "abc", which the length is 3.
>     Given "bbbbb", the answer is "b", with the length of 1.
>     Given "pwwkew", the answer is "wke", with the length of 3.
>
> Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



***

## Solution

*Using Two Pointers and Hash Table*

**Result:** Accepted **Time:** 16ms

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const int len = s.length();
        const char * chr = s.c_str();
        int have[256]={0}, ans = 0;
        for(int left = 0, right = 0; right < len ; right ++)
        {
            if(++have[chr[right]] == 2)
            {
                do{
                    have[chr[left]] --;
                }while(!have[chr[left++]]);
            }
            else if(ans <= right - left)
                ans = right - left + 1;
        }
        return ans;
    }
};
```

*Another Two Pointers and Hash Table Way with while Loop*

**Result:** Accepted **Time:** 12ms

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const int len = s.length();
        const char * chr = s.c_str();
        int ans = 0,i = 0,j = 0;
        bool have[256]={1,0};
        while(j < len)
        {
            while(!have[chr[j]])
                have[chr[j++]] = true;
            if( ans < j - i)
                ans = j - i;
            while(chr[i] != chr[j])
                have[chr[i++]] = false;
            ++j,++i;
        }
        return ans;
    }
};
```

*Another Hash Table Way*

**Result:** Accepted **Time:** 8ms

```c
int lengthOfLongestSubstring(char* s) {
    int index[256]={0},ret = 0;
    for(int i = 0,last = 0;  s[i]; i++)
    {
        if(last < index[s[i]])
            last = index[s[i]];
        if(ret <= i - last)
            ret = i - last + 1;
        index[s[i]] = i + 1;
    }
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n))$$
- Space Complexity: $$O(1)$$
