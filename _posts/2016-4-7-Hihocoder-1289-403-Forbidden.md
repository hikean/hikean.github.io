---
layout: post
title:  Hihocoder 1289 403 Forbidden
categories: [题解]
tags: [OJ, 校园招聘, Microsoft, 微软在线笔试, Hihocoder, Trie Tree, 数据结构]
excerpt: "2016年微软校园招聘在线笔试第二题，数据结构题，使用Trie树或STL map均可解"
---



* Contents
{:toc #toc_of_keans_blog}


时间限制:10000ms
单点时限:1000ms
内存限制:256MB

## 描述

Little Hi runs a web server. Sometimes he has to deny access from a certain set of malicious IP addresses while his friends are still allow to access his server. To do this he writes N rules in the configuration file which look like:

```
allow 1.2.3.4/30
deny 1.1.1.1
allow 127.0.0.1
allow 123.234.12.23/3
deny 0.0.0.0/0
```

Each rule is in the form:
allow | deny address or allow | deny address/mask.

When there comes a request, the rules are checked in sequence until the first match is found. If no rule is matched the request will be allowed. Rule and request are matched if the request address is the same as the rule address or they share the same first mask digits when both written as 32bit binary number.

For example IP "1.2.3.4" matches rule "allow 1.2.3.4" because the addresses are the same. And IP "128.127.8.125" matches rule "deny 128.127.4.100/20" because 10000000011111110000010001100100 (128.127.4.100 as binary number) shares the first 20 (mask) digits with 10000000011111110000100001111101 (128.127.8.125 as binary number).

Now comes M access requests. Given their IP addresses, your task is to find out which ones are allowed and which ones are denied.

## 输入

Line 1: two integers N and M.
Line 2-N+1: one rule on each line.
Line N+2-N+M+1: one IP address on each line.
All addresses are IPv4 addresses(0.0.0.0 - 255.255.255.255). 0 <= mask <= 32.

For 40% of the data: $$1 <= N, M <= 1000$$.
For 100% of the data: $$1 <= N, M <= 100000$$.

## 输出

For each request output "YES" or "NO" according to whether it is allowed.

## 样例输入

```
5 5
allow 1.2.3.4/30
deny 1.1.1.1
allow 127.0.0.1
allow 123.234.12.23/3
deny 0.0.0.0/0
1.2.3.4
1.2.3.5
1.1.1.1
100.100.100.100
219.142.53.100
```

## 样例输出

```
YES
YES
NO
YES
NO
```

## 解题思路

> 普通青年用Tire树，也可以用map

## 二叉树版（不算严格的Trie树)

```cpp
#include <stdio.h>
#include <string.h>

#define INDEX(i) data[i].left

#define ALLOW(i,msk) (infos[INDEX(i)][msk][0])
#define ID(i,msk)  (infos[INDEX(i)][msk][1])

struct Node{
    int left,right;
    Node():left(0),right(0){};
    Node(int l,int r):left(l),right(r){}
};

const int MAXN = 100000 * 40;
Node data[MAXN];
int infos[(1<<17)][33][2];
int icnt = 1;
int cnt = 1;

void add_node(unsigned int ip,int allow,int id,int msk)
{
    unsigned  int mask = 0x80000000;
    int root = 0;
    while(mask)
    {
        if(ip & mask)// 1
        {
            if(data[root].right == 0)
                data[root].right = cnt++;
            root = data[root].right;
        }
        else // 0
        {
            if(data[root].left == 0)
                data[root].left = cnt++;
            root = data[root].left;
        }
        mask >>= 1;
    }
    if(!INDEX(root))
        INDEX(root) = icnt++;
    if(!ID(root,msk))
    {
        ID(root,msk) = id;
        ALLOW(root,msk) = allow;
    }
}

int find_node(unsigned int ip,int msk)
{
    unsigned  int mask = 0x80000000;
    int root = 0;
    while(mask)
    {
        if(ip & mask)// 1
        {
            if(data[root].right == 0)
                return 0;
            root = data[root].right;
        }
        else
        {
            if(data[root].left == 0)
                return 0;
            root = data[root].left;
        }
        mask >>= 1;
    }

    return root;
}

int main()
{
    unsigned  int mask[33];
    mask[0] = 0xffffffff;
    for(int  i = 1; i < 33; i++)
        mask[i] = mask[i-1] << 1;
    memset(infos,0,sizeof(infos));
    int m,n;
    unsigned  int tmp,ans;
    char str[50],ip[50];
    scanf("%d%d",&n,&m);
    for(int j = 0; j < n; j++)
    {
        scanf("%s%s",str,ip);
        int i = 0;
        ans = 0;
        tmp = 0;
        for(;ip[i]!='/' && ip[i]!='\0'; i++)
            if(ip[i] == '.')
            {
                ans = (ans << 8) | tmp;
                tmp = 0;
            }
            else
                tmp = tmp*10 + ip[i] - '0';
        ans = (ans << 8) | tmp;
        tmp = 32;
        if(ip[i] == '/')
        {
            tmp = 0;
            for(i += 1;ip[i]!='\0';i++)
                tmp = tmp * 10 + ip[i] - '0';
            ans = ans & mask[32-tmp];
        }
        add_node(ans,str[0]=='a',j+1,tmp);
    }
    for(int i = 0; i < m; i++)
    {
        scanf("%s",ip);
        ans = 0;
        tmp = 0;
        for(int j= 0;ip[j] != '\0'; j++)
            if(ip[j] == '.')
            {
                ans = (ans << 8) | tmp;
                tmp = 0;
            }
            else
                tmp = tmp*10 +ip[j] - '0';
        ans = (ans << 8) | tmp;
        int index = 0;
        int id = MAXN;
        int mk = 32;
        for(int j = 0 ; j < 33; j++)
        {
            tmp = ans & mask[j];
            int t = find_node(tmp,32-j);
            if(t && ID(t,32-j) &&  ID(t,32-j) < id)
                index = t,id = ID(t,32-j),mk = 32 -j;
        }
        if(!index || ALLOW(index,mk))
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}

/***
5 5

deny 0.0.0.0
allow 0.0.0.1/28
allow 0.0.0.255/28
allow 0.0.0.0
deny 0.0.0.0/24
1.2.3.4
1.2.3.5
1.1.1.1
0.0.0.1
0.0.0.0


***/

```

## map版

```cpp
#include <stdio.h>
#include <map>

using std::map;

map<long long,int> dat;

int main()
{
    unsigned  int mask[33];
    mask[0] = 0xffffffff;
    for(int  i = 1; i < 33; i++)
        mask[i] = mask[i-1] << 1;
    int m,n;
    unsigned  int tmp,ans;
    char str[50],ip[50];
    scanf("%d%d",&n,&m);
    for(int j = 0; j < n; j++)
    {
        scanf("%s%s",str,ip);
        int i = 0;
        ans = 0;
        tmp = 0;
        for(;ip[i]!='/' && ip[i]!='\0'; i++)
            if(ip[i] == '.')
            {
                ans = (ans << 8) | tmp;
                tmp = 0;
            }
            else
                tmp = tmp*10 + ip[i] - '0';
        ans = (ans << 8) | tmp;
        tmp = 32;
        if(ip[i] == '/')
        {
            tmp = 0;
            for(i += 1;ip[i]!='\0';i++)
                tmp = tmp * 10 + ip[i] - '0';
            ans = ans & mask[32-tmp];
        }
        long long key = 0;
        key |= ans;
        key = (key << 8) | tmp;

        if(!dat.count(key))
            dat[key] = (j << 8) | str[0]=='a';
    }
    for(int i = 0; i < m; i++)
    {
        scanf("%s",ip);
        ans = 0;
        tmp = 0;
        for(int j= 0;ip[j] != '\0'; j++)
            if(ip[j] == '.')
            {
                ans = (ans << 8) | tmp;
                tmp = 0;
            }
            else
                tmp = tmp*10 +ip[j] - '0';
        ans = (ans << 8) | tmp;
        long long key = 0;
        int id = 0x3fffffff;
        for(int j = 0 ; j < 33; j++)
        {
            tmp = ans & mask[j];
            key = tmp;
            key = (key << 8) | (32-j);
            if(dat.count(key) && dat[key] < id)
                id = dat[key];
        }
        if(id & 1)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}

/***
5 5

deny 0.0.0.0
allow 0.0.0.1/28
allow 0.0.0.255/28
allow 0.0.0.0
deny 0.0.0.0/24
1.2.3.4
1.2.3.5
1.1.1.1
0.0.0.1
0.0.0.0

***/
```
