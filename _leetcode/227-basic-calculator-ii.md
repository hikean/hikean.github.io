---
layout: leetcode
date: 2016-07-16
title: Basic Calculator II
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
<pre>
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
</pre>

**Note: Do not** use the `eval` built-in library function.




***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c

#include <stdio.h>
#include <ctype.h>

int getlv(char ch)
{
    switch(ch)
    {
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 2;
    default:
       return 0;
    }
}

int  operate(int a ,int b,char tmp)
{
    ///printf(" %d %c % d\n",a,tmp,b);
    switch (tmp)
    {
    case '+':
        return a + b;
    case '-':
       return a - b;
    case '*':
        return a * b;
    case '/':
       return a/b;
    }
}

int deal(const char data[])
{
    char sta[100],tmp;
    int top=0,ptr=0;
    int ans[100],atop=0;
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
        if(top == 0)
            sta[top++] = tmp;
        else if((tmp=='-'||tmp=='+'||tmp=='*'||tmp=='/'))
        {
            int curlv=getlv(tmp);
            int stalv=getlv(sta[top-1]);
            while(curlv<=stalv)
            {
                ans[atop - 2] = operate(ans[atop -2],ans[atop - 1],sta[--top]);
                atop --;
                if(atop>0)
                    stalv=getlv(sta[top-1]);
                else
                    break;
            }
            sta[top++] = tmp;
        }
    }
    while(top > 0)
    {
        ans[atop - 2] = operate(ans[atop -2],ans[atop - 1],sta[--top]);
        atop --;
    }
    ///printf("%d\n",ans[0]);
    return ans[0];
}


int calculate(char* data)
{
    return deal(data);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
