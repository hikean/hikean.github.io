---
layout: leetcode
date: 2016-07-16
title: Valid Anagram
tags: [Hash Table, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,

s = ``"anagram"``, t = ``"nagaram"``, return `true`.

s = ``"rat"``, t = ``"car"``, return `false`.

**Note:**

You may assume the string contains only lowercase alphabets.

**Follow up:**

What if the inputs contain unicode characters? How would you adapt your solution to such case?


***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
bool isAnagram(char* s, char* t) {
     int have[256]={0};
     while(*s) have[*(s++)]++;
     while(*t) have[*(t++)]--;
     for(char tmp = 'a';tmp <= 'z'; ++tmp)
         if(have[tmp])
            return false;
     return true;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
