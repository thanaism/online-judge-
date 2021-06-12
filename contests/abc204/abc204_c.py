from collections import deque,defaultdict
n,m=map(int,input().split())
l=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    l[a-1].append(b-1)
ans=0
for i in range(n):
    seen=[0]*n
    q=deque()
    q.append(i)
    while q:
        x=q.popleft()
        seen[x]=1
        for j in l[x]:
            if seen[j]==0:q.append(j)
    ans+=sum(seen)
print(ans)

        

    