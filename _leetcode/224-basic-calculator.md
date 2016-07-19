---
layout: leetcode
date: 2016-07-16
title: Basic Calculator
tags: [Stack, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, **non-negative** integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

    "1 + 1" = 2
    " 2-1 + 2 " = 3
    "(1+(4+5+2)-3)+(6+8)" = 23

**Note: Do not** use the `eval` built-in library function.


***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int operate(int a ,int b,char tmp)
{
    if(tmp == '-')
        return a - b;
    return a +  b;
}

int deal(const char data[])
{
    char sta[1000],tmp;
    int top=0,ptr=0;
    int ans[1000],atop=0;
    int value=0;
    while(data[ptr]!='\0')
    {
        if(isdigit(data[ptr]))
        {
            value = 0;
            while(data[ptr]>='0'&&data[ptr]<='9')
                value = value * 10 + data[ptr++] - '0';
            ans[atop++] = value;
        }
        tmp=data[ptr++];
        if(tmp=='\0') break;
        if(tmp == ')')
        {
            while(sta[top - 1] != '(')
            {
                ans[atop - 2] = operate(ans[atop -2],ans[atop - 1],sta[--top]);
                atop --;
            }
            top--;
            continue;
        }

        if((top == 0 && tmp !=' ') || tmp =='(')
            sta[top++] = tmp;
        else if((tmp=='-'||tmp=='+'))
        {
            while(top && sta[top - 1]!='(')
            {
                ans[atop - 2] = operate(ans[atop -2],ans[atop - 1],sta[--top]);
                atop --;
            }
            sta[top++] = tmp;
        }
    }
    while(top > 0)
    {
        ans[atop - 2] = operate(ans[atop -2],ans[atop - 1],sta[--top]);
        atop --;
    }
   // printf("%d\n",ans[0]);
    return ans[0];
}

int calculate(char* s) {
    return deal(s);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
