---
layout: post
title: Hihocoder 1290 Demo Day
categories: [题解]
tags: [OJ, 校园招聘, Microsoft, 微软在线笔试, Hihocoder, DP, SPFA]
excerpt: "2016年微软校园招聘在线笔试第一题，使用DP或者SPFA均可解"
---


* Contents
{:toc #toc_of_keans_blog}


时间限制:10000ms
单点时限:1000ms
内存限制:256MB

## 描述

You work as an intern at a robotics startup. Today is your company's demo day. During the demo your company's robot will be put in a maze and without any information about the maze, it should be able to find a way out.

The maze consists of N * M grids. Each grid is either empty(represented by '.') or blocked by an obstacle(represented by 'b'). The robot will be release at the top left corner and the exit is at the bottom right corner.

Unfortunately some sensors on the robot go crazy just before the demo starts. As a result, the robot can only repeats two operations alternatively: keep moving to the right until it can't and keep moving to the bottom until it can't. At the beginning, the robot keeps moving to the right.

```
rrrrbb..            
...r....     ====> The robot route with broken sensors is marked by 'r'.
...rrb..
...bb...
```
While the FTEs(full-time employees) are busy working on the sensors, you try to save the demo day by rearranging the maze in such a way that even with the broken sensors the robot can reach the exit successfully. You can change a grid from empty to blocked and vice versa. So as not to arouse suspision, you want to change as few grids as possible. What is the mininum number?

## 输入

Line 1: N, M.
Line 2-N+1: the N * M maze.
For 20% of the data, N * M <= 16.
For 50% of the data, 1 <= N, M <= 8.
For 100% of the data, 1<= N, M <= 100.

## 输出

The minimum number of grids to be changed.

**样例输入**

```
4 8
....bb..
........
.....b..
...bb...
```

**样例输出**

```
1
```

## 解题思路

> 主要是dp和SPFA

## SPFA-1

```cpp
#include <stdio.h>
#include <queue>
#include <string.h>

using std::priority_queue;
const int RIGHT = 0;
const int DOWN = 1;


struct State
{
  int x,y;
  int cost;
  int dir;
  State(int _x,int _y,int l,int d):x(_x),y(_y),cost(l),dir(d){}
  State():x(0),y(0),cost(0),dir(RIGHT){}
  bool operator < (const State & arg) const
  {
    return this->cost > arg.cost;
  }
};

const int  MAXN = (100+5);


char maze[MAXN][MAXN];
int  vis[MAXN][MAXN][2];



int main()
{
  int n,m;
  scanf("%d%d",&n,&m);
  for(int i = 0; i < n; i++)
  scanf("%s",maze[i]);
  memset(vis,0x3f,sizeof(vis));
  priority_queue<State> que;
  que.push(State(0,0,0,RIGHT));
  State now,down,right;
  int x,y;
  while(!que.empty())
  {
    now = que.top();que.pop();
    x = now.x;
    y = now.y;
    //printf("%d %d %d\n",x,y,now.cost);
    if(x == n-1 && y == m -1)
    {
      printf("%d\n",now.cost);
      break;
    }
    down = now;
    down.dir = DOWN;
    if(x + 1 < n)//down
    {
      //            if(y+1 < m && maze[x][y+1] != 'b' && now.dir == RIGHT)
      if( y + 1 < m && maze[x][y+1] == '.' && now.dir == RIGHT)
      down.cost  += 1;
      down.x += 1;
      if(maze[x+1][y] == 'b')
      down.cost += 1;
      if(down.cost < vis[down.x][down.y][DOWN])
      {
        que.push(down);
        vis[down.x][down.y][DOWN] = down.cost;
      }
    }
    right  = now;
    right.dir = RIGHT;
    if(y + 1 < m ) //right
    {
      if( x + 1 < n && maze[x+1][y] =='.'  && now.dir == DOWN)
      right.cost += 1;
      if(maze[x][y+1] == 'b')
      right.cost += 1;
      right.y += 1;
      if(right.cost < vis[right.x][right.y][RIGHT])
      {
        que.push(right);
        vis[right.x][right.y][RIGHT] = right.cost;
      }
    }
  }
  return 0;

}
/*

4 8
....bb..
........
.....b..
...bb...

4 8
.b..bb..
..b.....
b..b.b..
.b..bb..

4 8
.b..bb..
..b..b..
b..b.b..
.b..bb..

*/
```

## SPFA-2

```cpp
#include<cstdio>
#include<algorithm>
//  using namespace std;
#define R 105
#define N 40010
#define M 400000
const int inf=1000000;
#define rep(i,n) for (int i=1;i<=n;++i)
#define fr(i,x,y) for (int i=x;i<=y;++i)
int son[N];
int st[M],ed[M],next[M],cost[M];
int d[N];
int f[N*20];
int S,T,l;
bool b[N],v[N];
int id[R][R],idd;
char s[R][R];
int n,m;
void add(int x,int y,int z,int c)
{
  st[l]=x,ed[l]=y,cost[l]=c,next[l]=son[x],son[x]=l;l++;

}
void spfa()
{
  int h=0,t=1; rep(i,T+1) d[i-1]=inf;
  d[f[1]=S]=0;
  while (h<t){
    int x=f[++h]; b[x]=0;
    for (int p=son[x];p;p=next[p]){
      int y=ed[p];
      if (d[x]+cost[p]<d[y]){
        d[y]=d[x]+cost[p];
        if (!b[y]) b[y]=1,f[++t]=y;
      }

    }
  }
}
void work1()
{
  rep(i,T+1) son[i-1]=0;
  l=2;
  S=idd*4;
  T=S+1;
  add(S,id[1][1]*4+(s[1][1]=='.'?0:2),1,0);
  add(id[n][m]*4+0,T,1,0);
  add(id[n][m]*4+1,T,1,0);

  fr(i,1,n)fr(j,1,m)
  {
    add(id[i][j]*4+0,id[i][j]*4+2,1,1),
    add(id[i][j]*4+1,id[i][j]*4+3,1,1),
    add(id[i][j]*4+2,id[i][j]*4+0,1,1),
    add(id[i][j]*4+3,id[i][j]*4+1,1,1);
  }
  fr(i,1,n)fr(j,1,m-1)
  {
    add(id[i][j]*4+0,id[i][j+1]*4+(s[i][j+1]=='.'?0:2),1,0);
    if (i>1)add(id[i][j]*4+3,id[i-1][j+1]*4+(s[i-1][j+1]=='.'?0:2),1,0);
  }
  fr(i,1,n-1)fr(j,1,m)
  {
    add(id[i][j]*4+1,id[i+1][j]*4+(s[i+1][j]=='.'?1:3),1,0);
    if (j>1)    add(id[i][j]*4+2,id[i+1][j-1]*4+(s[i+1][j-1]=='.'?1:3),1,0);
  }

  fr(i,1,n)fr(j,m,m)
  {
    add(id[i][j]*4+0,id[i][j]*4+1,1,0);
    //add(id[i][j]*4+1,id[i][j]*4+0,1,0);
  }
  fr(i,n,n)fr(j,1,m)
  {
    //add(id[i][j]*4+0,id[i][j]*4+1,1,0);
    add(id[i][j]*4+1,id[i][j]*4+0,1,0);
  }
  spfa();
  printf("%d\n",d[T]);
}

int main()
{   scanf("%d%d",&n,&m);
fr(i,1,n)
scanf("%s",s[i]+1);
idd=0;
fr(i,1,n)
fr(j,1,m)
{
  id[i][j]=idd++;
}
work1();


}
/*
4 8
....bb..
........
.....b..
...bb...
*/
```
> 致谢CHM童鞋
