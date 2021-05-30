import sys;sys.setrecursionlimit(500000)
n,m=map(int,input().split())
g0=[[] for _ in range(n)]
g1=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    g0[a].append(b)
    g1[b].append(a)

def dfs0(i):
    seen[i]=True
    for e in g0[i]:
        if not seen[e]: dfs0(e)
    order.append(i)

def dfs1(i):
    seen[i]=True
    global cnt
    cnt+=1
    for e in g1[i]:
        if not seen[e]: dfs1(e)
    
seen=[False]*n
order=[]
for i in range(n):
    if not seen[i]: dfs0(i)
ans=0
for i in range(n): seen[i]=False
for i in reversed(order):
    if seen[i]: continue
    cnt=0
    dfs1(i)
    ans+=cnt*(cnt-1)//2
print(ans)