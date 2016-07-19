---
layout: leetcode
date: 2016-07-15
title: Reverse Words in A String
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an input string, reverse the string word by word.
>
>For example,
>
>Given s = `"the sky is blue"`,
>
>return `"blue is sky the"`.
>     
>**Note:** For C programmers: Try to solve it in-place in O(1) space.
>

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
void reverse(char * s,int first, int last)
{
    while(first < last)
    {
        char tmp = s[first];
        s[first++] = s[last];
        s[last--] = tmp;
    }
}
void reverseWords(char *s) {
    int last = 0, now = 0,i;
    while(s[now])
    {
        while(s[last = now] == ' ') now++;
        while( s[now] != ' ' && s[now]!= '\0') now++;
        reverse(s,last,now-1);
    }
    reverse(s,0,now-1);
    for(last = i = 0; i <= now; i++)/// delete duplicated blank
        if(!isblank(s[i]) ||(last && s[last-1]!=s[i]) )
            s[last++] = s[i];
    if(--last && s[last - 1] ==' ')/// delete last blank
        s[last - 1] = 0;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
