n,k=map(int,input().split())
a=[*map(int,input().split())]
from collections import defaultdict
d=defaultdict(int)
for i in a:
    d[i]+=1
ans=[0]*k
for i in range(n+1):
    for j in range(min(d[i],k)):
        if ans[j]==i:ans[j]+=1
print(sum(ans))