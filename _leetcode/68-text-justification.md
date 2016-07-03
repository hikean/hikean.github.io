---
layout: leetcode
date: 2016-06-28
title: Text Justification
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
>
> You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
>
>Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
>
>For the last line of text, it should be left justified and no extra space is inserted between words.
>
>For example,
>
> words: `["This", "is", "an", "example", "of", "text", "justification."]``
>
> L: `16`.
>
> Return the formatted lines as:
>   
>     [
>        "This    is    an",
>        "example  of text",
>        "justification.  "
>     ]
>
> **Note:** Each word is guaranteed not to exceed L in length.
>

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        int n = (int)words.size(), out = 0;
        vector<string> result;
        while (out < n) {
            int i = out, curWidth = (int)words[i++].size();
            while (i < n && curWidth + 1 + (int)words[i].size() <= maxWidth)
                curWidth += 1 + (int)words[i++].size();
            int numExtraSpace = maxWidth - curWidth;
            string ss = words[out++];
            for (int pad = 0; out < i; out++) {
                if (i < n)
                    pad = numExtraSpace / (i-out) + (numExtraSpace % (i-out) ? 1 : 0);
                ss += string(pad+1,' ');
                numExtraSpace -= pad;
                ss += words[out];
            }
            ss+= string(numExtraSpace,' ');
            result.push_back(ss);
        }
        return result;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
