---
layout: leetcode
date: 2016-07-15
title: Evaluate Reverse Polish Notation
tags: [Stack]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Evaluate the value of an arithmetic expression in Reverse Polish Notation.
>
> Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.
>
>Some examples:
>
>       ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
>       ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
>
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int stck[10240];
int operate(int a, int b, char tmp)
{
    if(tmp == '-') return a - b;
    if(tmp == '+') return a + b;
    if(tmp == '*') return a * b;
    return a / b;
}
int evalRPN(char** tokens, int tokensSize) {
    for(int i = 0,top = -1; i < tokensSize; i++)
        if(isdigit(tokens[i][0]) || (tokens[i][0] == '-' && tokens[i][1]))
            stck[++top] = atoi(tokens[i]);
        else
            stck[--top] = operate(stck[top] ,stck[top+1],tokens[i][0]);
    return stck[0];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
