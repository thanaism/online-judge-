from collections import deque,defaultdict
n=int(input())
edge=defaultdict(list)
cost=defaultdict(list)
for _ in range(n-1):
    u,v,w=map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
    cost[u].append(w)
    cost[v].append(w)
dist=defaultdict(lambda:-1)
dist[1]=0
que=deque([1])
while que:
    now=que.popleft()
    for i in range(len(edge[now])):
        nxt=edge[now][i]
        if dist[nxt]==-1:
            dist[nxt]=dist[now]^cost[now][i]
            que.append(nxt)
MOD=10**9+7
ans=0
for i in range(60):
    cnt=[0]*2
    for j in range(n):
        cnt[dist[j+1]>>i&1]+=1
    ans+=(1<<i)*cnt[0]*cnt[1]
    ans%=MOD
print(ans)