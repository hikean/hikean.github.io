---
layout: post
title:  微软2016校园招聘4月在线笔试题
categories: [Coding]
tags: [Coding, Algorithm, 校园招聘, 在线笔试, Microsoft微软 ]
---

<!-- more --> 微软2016校园招聘4月在线笔试题，全部四题，全部提交通过了<!-- more -->



* Contents
{:toc #toc_of_keans_blog}


## 1288 : Font Size

时间限制:10000ms
单点时限:1000ms
内存限制:256MB

### 描述

Steven loves reading book on his phone. The book he reads now consists of N paragraphs and the i-th paragraph contains ai characters.
Steven wants to make the characters easier to read, so he decides to increase the font size of characters. But the size of Steven's phone screen is limited. Its width is W and height is H. As a result, if the font size of characters is S then it can only show ⌊W / S⌋ characters in a line and ⌊H / S⌋ lines in a page. (⌊x⌋ is the largest integer no more than x)  
So here's the question, if Steven wants to control the number of pages no more than P, what's the maximum font size he can set? Note that paragraphs must start in a new line and there is no empty line between paragraphs.

### 输入

Input may contain multiple test cases.
The first line is an integer TASKS, representing the number of test cases.
For each test case, the first line contains four integers N, P, W and H, as described above.
The second line contains N integers a1, a2, ... aN, indicating the number of characters in each paragraph.
For all test cases,
  $$1 <= N <= 10^3$$
  $$1 <= W, H, ai <= 10^3$$
  $$1 <= P <= 10^6$$
There is always a way to control the number of pages no more than P.


### 输出

For each testcase, output a line with an integer Ans, indicating the maximum font size Steven can set.

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

### 解题思路

> 好像暴力都可以过，不过还是二分是正道（二分写的渣了点。。。）

### 代码

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

## 1289 : 403 Forbidden

时间限制:10000ms
单点时限:1000ms
内存限制:256MB

### 描述

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

### 输入

Line 1: two integers N and M.
Line 2-N+1: one rule on each line.
Line N+2-N+M+1: one IP address on each line.
All addresses are IPv4 addresses(0.0.0.0 - 255.255.255.255). 0 <= mask <= 32.

For 40% of the data: $$1 <= N, M <= 1000$$.
For 100% of the data: $$1 <= N, M <= 100000$$.

### 输出

For each request output "YES" or "NO" according to whether it is allowed.

### 样例输入

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

### 样例输出

```
YES
YES
NO
YES
NO
```

### 解题思路

> 普通青年用Tire树，也可以用map

### Tire树版，二叉树版

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

### map版

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


##  1290 : Demo Day

时间限制:10000ms
单点时限:1000ms
内存限制:256MB

### 描述

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

### 输入

Line 1: N, M.
Line 2-N+1: the N * M maze.
For 20% of the data, N * M <= 16.
For 50% of the data, 1 <= N, M <= 8.
For 100% of the data, 1<= N, M <= 100.

### 输出

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

### 解题思路

> 主要是dp和SPFA

### SPFA-1

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

### SPFA-2

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

## 1291 : Buiding in Sandbox

时间限制:30000ms
单点时限:3000ms
内存限制:256MB

### 描述
Little Hi is playing a sandbox voxel game. In the game the whole world is constructed by massive 1x1x1 cubes. The edges of cubes are parallel to the coordinate axes and the coordinates (x, y, z) of the center of each cube are integers.

![_config.yml]({{ site.baseurl }}/images/posts/2016/4/16_4_7_1.jpg)

At the beginning there is nothing but plane ground in the world. The ground consists of all the cubes of z=0. Little Hi needs to build everything by placing cubes one by one following the rules:

1. The newly placed cube must be adjacent to the ground or a previously placed cube. Two cubes are adjacent if and only if they share a same face.

2. The newly placed cube must be accessible from outside which means by moving in 6 directions(up, down, left, right, forward, backward) there is a path from a very far place - say (1000, 1000, 1000) in this problem - to this cube without passing through ground or other cubes.

Given a sequence of cubes Little Hi wants to know if he can build the world by placing the cubes in such order.

### 输入
The first line contains the number of test cases T(1 <= T <= 10).
For each test case the first line is N the number of cubes in the sequence.
The following N lines each contain three integers x, y and z indicating the coordinates of a cube.
For 20% of the data, 1 <= N <= 1000, 1 <= x, y, z <= 10.
For 100% of the data, 1 <= N <= 100000, 1 <= x, y, z <= 100.

### 输出
For each testcase output "Yes" or "No" indicating if Little Hi can place the cubes in such order.

### 样例提示
In the first test case three cubes are placed on the ground. It's OK.
In the second test case (1, 3, 2) is neither on the ground nor adjacent to previous cubes. So it can't be placed.
In the last test case (2, 2, 1) can not be reached from outside. So it can't be placed.  

**样例输入**

```
3
3
1 1 1
1 2 1
1 3 1
3
1 1 1
1 2 1
1 3 2
17
1 1 1
1 2 1
1 3 1
2 3 1
3 3 1
3 2 1
3 1 1
2 1 1
2 1 2
1 1 2
1 2 2
1 3 2
2 3 2
3 3 2
3 2 2
2 2 2
2 2 1
```

**样例输出**

```
Yes
No
No
```

### 解题思路
> BFS

### 代码

```cpp
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>

using std::max;
using std::queue;
const int MAXN = 128;
const int OUTER = 0x3fffffff;
int cube[MAXN][MAXN][MAXN];
int cnt=0;
int vis[MAXN][MAXN][MAXN]={0};
int data[100000 + 5][3];

const int dx[] = { 0, 0, 1,-1, 0, 0};
const int dy[] = { 0, 0, 0, 0, 1,-1};
const int dz[] = { 1,-1, 0, 0, 0, 0};
bool bfs(int x,int y,int z,int lim);

struct State{
  int x,y,z;
  State():x(0),y(0),z(0){}
  State(int a,int b,int c):x(a),y(b),z(c){}
};

bool adjacent(int x,int y,int z)
{
  int a,b,c;
  if(z == 1) return true;
  for(int i = 0; i < 6; i++)
  {
    a = x + dx[i];
    b = y + dy[i];
    c = z + dz[i];
    if( a > 0 && b > 0 && c > 0 && cube[a][b][c])
    return true;
  }
  return false;
}

int main()
{
  int t,x,y,z,flag,lim;
  scanf("%d",&t);
  while(t--)
  {
    lim  = 0;
    flag = 1;
    scanf("%d",&cnt);
    memset(cube,0,sizeof(cube));
    memset(vis,0,sizeof(vis));
    for(int i = 0; i < cnt; i++)
    {
      scanf("%d%d%d",&x,&y,&z);
      if(!adjacent(x,y,z))
      {
        //printf("err: %d %d %d \n",x,y,z);
        flag = 0;
      }
      cube[x][y][z] = (i + 1);
      data[i][0] = x;
      data[i][1] = y;
      data[i][2] = z;
      lim = max(max(lim,x),max(y,z));
    }
    lim += 2;
    if(flag)
    {
      cube[lim][lim][lim] = cnt + 1;
      bfs(lim,lim,lim,lim);
      while(cnt-- && flag)
      flag = bfs(data[cnt][0],data[cnt][1],data[cnt][2],lim);
    }
    if(flag)
    puts("Yes");
    else
    puts("No");
  }
  return 0;
}

bool bfs(int x,int y,int z,int lim)
{
  queue<State> * que_ptr = new queue<State>();
  queue<State>  & que = *que_ptr;
  que.push(State(x,y,z));
  const int value = cube[x][y][z];
  cube[x][y][z] = OUTER;
  vis[x][y][z] = value;
  bool ret = false;
  State now;
  int a,b,c;
  while(!que.empty())
  {
    now = que.front(); que.pop();
    x = now.x;
    y = now.y;
    z = now.z;
    for(int i = 0; i < 6; i++)
    {
      a = x + dx[i];
      b = y + dy[i];
      c = z + dz[i];
      if( a < 0 || b < 0 || c < 1 || a > lim || b > lim || c > lim)
      continue;
      if(vis[a][b][c] != value && cube[a][b][c] == OUTER)
      ret = true;
      if(vis[a][b][c] || cube[a][b][c])
      continue;
      vis[a][b][c] = value;
      cube[a][b][c] = OUTER;
      que.push(State(a,b,c));
    }
  }
  delete que_ptr;
  return ret;
}

/**

5
3
1 1 1
1 2 1
1 3 2
17
1 1 1
1 2 1
1 3 1
2 3 1
3 3 1
3 2 1
3 1 1
2 1 1

2 1 2
1 1 2
1 2 2
1 3 2
2 3 2
3 3 2
3 2 2
2 2 2
2 2 1

**/
```
