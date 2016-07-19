---
layout: leetcode
date: 2016-07-18
title: Reverse Vowels of a String
tags: [String, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Write a function that takes a string as input and reverse only the vowels of a string.

**Example 1:**

Given s = `"hello"`, return `"holle"`.

**Example 2:**

Given s = `"leetcode"`, return `"leotcede"`.



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c

static bool is_vowels[256]={0};
static bool is_init = false;
char vowels[]="euioaEUIOA";

char* reverseVowels(char* s) {
    if(!is_init)
    {
        is_init = true;
        for(int i = 0; vowels[i]!='\0';i++)
            is_vowels[vowels[i]] = true;
    }
    int low = 0;
    int up = strlen(s);
    char tmp;
    while(low < up)
    {
        while(low < up && !is_vowels[s[low]])
            low ++;
        while(low < up && !is_vowels[s[up]])
            up --;
        if(low < up)
        {
            tmp = s[low];
            s[low++] = s[up];
            s[up--] = tmp;
        }
    }
    
    return s;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
