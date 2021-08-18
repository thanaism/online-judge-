n,k=map(int,input().split())
c=[*map(int,input().split())]
from collections import defaultdict
d=defaultdict(int)
s=set()
for i in range(k):
	d[c[i]]+=1
	s.add(c[i])
ans=len(s)
for i in range(k,n):
	d[c[i]]+=1
	if d[c[i]]==1:s|={c[i]}
	d[c[i-k]]-=1
	if d[c[i-k]]==0:s-={c[i-k]}
	ans=max(ans,len(s))
print(ans)