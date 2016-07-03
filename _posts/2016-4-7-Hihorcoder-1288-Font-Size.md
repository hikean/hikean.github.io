---
layout: post
title:  Hihocoder 1288 Font Size
categories: [题解]
tags: [OJ, 校园招聘, Microsoft, 微软在线笔试, Hihocoder, Binary Search]
excerpt: "2016年微软校园招聘在线笔试第一题，简单的二分搜索题"
---



* Contents
{:toc #toc_of_keans_blog}


时间限制:10000ms
单点时限:1000ms
内存限制:256MB

## 描述

Steven loves reading book on his phone. The book he reads now consists of N paragraphs and the i-th paragraph contains ai characters.
Steven wants to make the characters easier to read, so he decides to increase the font size of characters. But the size of Steven's phone screen is limited. Its width is W and height is H. As a result, if the font size of characters is S then it can only show ⌊W / S⌋ characters in a line and ⌊H / S⌋ lines in a page. (⌊x⌋ is the largest integer no more than x)  
So here's the question, if Steven wants to control the number of pages no more than P, what's the maximum font size he can set? Note that paragraphs must start in a new line and there is no empty line between paragraphs.

## 输入

Input may contain multiple test cases.
The first line is an integer TASKS, representing the number of test cases.
For each test case, the first line contains four integers N, P, W and H, as described above.
The second line contains N integers a1, a2, ... aN, indicating the number of characters in each paragraph.
For all test cases,
  $$1 <= N <= 10^3$$
  $$1 <= W, H, ai <= 10^3$$
  $$1 <= P <= 10^6$$
There is always a way to control the number of pages no more than P.


## 输出

For each test case, output a line with an integer Ans, indicating the maximum font size Steven can set.

**样例输入**


```
2
1 10 4 3
10
2 10 4 3
10 10
```

**样例输出**

```
3
2
```

## 解题思路

> 好像暴力都可以过，不过还是二分是正道（二分写的渣了点。。。）

## 代码

```cpp
#include <stdio.h>
#include <algorithm>

using std::min;
using std::max;

int data[10000];

int check(int n, int para,int w,int h)
{
  int ret = 0;
  int w_cnt = w/n;
  int l_cnt = h/n;
  if(!w_cnt || !l_cnt)
  return 0x3fffffff;
  for(int i = 0; i < para; i++)
  ret += (data[i] + w_cnt - 1)/w_cnt;
  ret = (ret + l_cnt - 1)/l_cnt;
  return ret;
}

int main()
{
  int T, para, page,w,h;
  scanf("%d",&T);
  while(T--)
  {
    scanf("%d%d%d%d",&para,&page,&w,&h);
    for(int i = 0; i < para; i++)
    scanf("%d",&data[i]);
    int low = 1, up = min(w,h);
    int cnt,mid = 1,ans = 0;
    while(low <= up)
    {
      mid = (low + up) / 2;
      cnt = check(mid,para,w,h);
      if(cnt > page)
      up = mid -1;
      else
      {
        ans = mid;
        low = mid + 1;
      }
    }
    printf("%d\n",ans);
  }
  return 0;
}
```
