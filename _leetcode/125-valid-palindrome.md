---
layout: leetcode
date: 2016-07-11
title: Valid Palindrome
tags: [Two Pointers, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
>
>For example,
>
>`"A man, a plan, a canal: Panama"` is a palindrome.
>
>`"race a car"` is not a palindrome.
>
>**Note:**
>
>Have you consider that the string might be empty? This is a good question to ask during an interview.
>
>For the purpose of this problem, we define empty string as valid palindrome.
>
>    

***

## Solution

**Result:** Accepted **Time:** 6 ms

Here should be some explanations.

```c
bool isPalindrome(char* s) {
    int len = strlen(s);
    char * str = malloc(sizeof(char) * len + 5);
    char * tmp = str;
    char * mstr = str;
    bool ans = true;
    while(*s)
    {
        if(isalnum(*s))
        {
            if(isdigit(*s))
                *tmp = *s;
            else
                *tmp = (*s) | 32;
            ++tmp;
        }
        s++;
    }
    tmp--;
    while(tmp > str)
    {
        if(*tmp != *str)
        {
            ans = false;
            break;
        }
        --tmp;
        ++str;
    }
    free(mstr);
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
