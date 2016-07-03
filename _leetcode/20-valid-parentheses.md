---
layout: leetcode
date: 2016-06-25
title: Valid Parentheses
tags: [Stack, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string containing just the characters `'('`, `')'`,`'{'` , `'}'`, `'['` and `']'`, determine if the input string is valid.
>
> The brackets must close in the correct order,`"()"`  and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not.
>


***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
bool isValid(char* s) {
     int top =0,ptr =0;
     char tmp;
     while(tmp=s[ptr])
     {
         if(tmp=='(' || tmp =='{' || tmp =='[')
             s[top++] = tmp;
         else if(tmp ==')')
         {
             if(top && s[top-1] == '(')
                top--;
            else return false;
         }
        else if(tmp =='}')
        {
            if(top && s[top-1] == '{')
                top--;
            else return false;
        }
        else if(tmp == ']')
        {
            if(top && s[top-1] == '[')
                top--;
            else return false;
        }
        ptr++;
     }
     return top == 0;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
