n=int(input())
n+=1
a=[0]+[*map(int,input().split())]
for i in range(1,n):a[i]+=a[i-1]
from collections import defaultdict
d=defaultdict(int)
for i in a:
    d[i]+=1
ans=0
for v in d.values():
    ans+=v*(v-1)//2
print(ans)