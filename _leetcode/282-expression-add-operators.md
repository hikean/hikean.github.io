---
layout: leetcode
date: 2016-07-17
title: Expression Add Operators
tags: [Divide and Conquer]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a string that contains only digits `0-9` and a target value, return all possibilities to add **binary** operators (not unary) ``+``, ``-``, or ``*`` between the digits so they evaluate to the target value.

Examples:

<pre>
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
</pre>




***

## Solution

**Result:** Accepted **Time:**   380ms

Here should be some explanations.

```c
#include <stdio.h>
#include <ctype.h>

typedef long long LL;
inline int getlv(char ch)
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

LL  operate(LL a ,LL b,char tmp)
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
    return 0;
}

bool deal(const char data[],const int target)
{
   // puts(data);
    char sta[100],tmp;
    int top=0,ptr=0,atop=1;
    LL ans[100]={0};
    LL value=0;
    while(data[ptr]!='\0')
    {
        if(isdigit(data[ptr]))
        {
            value = 0;
            if(isdigit(data[ptr+1]) && data[ptr] =='0' )/// pre zero
                return false;
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
    return ans[atop-1]==target;
}

class Solution {
public:
    void dfs(vector<string> & ret,char * buff, int cnt ,const char * str,const int target)
    {
        while(*str)
        {
            buff[cnt++] = *(str++);
            if(*str == 0)
            {
                 buff[cnt] =0;
                if(deal(buff,target))
                    ret.push_back(buff);
                return;
            }
            buff[cnt++] = '-';
            dfs(ret,buff,cnt,str,target);
              buff[cnt-1] = '+';
            dfs(ret,buff,cnt,str,target);
              buff[cnt-1] = '*';
            dfs(ret,buff,cnt,str,target);
            cnt--;
        }
    }

    vector<string> addOperators(string num, int target) {
        char buff[256],cnt =0;
        vector<string> ret;
        dfs(ret,buff,cnt,num.c_str(),target);
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
