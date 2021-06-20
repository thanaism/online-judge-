n=int(input())
a=[*map(int,input().split())]
from collections import defaultdict
d=defaultdict(int)
for i in a:d[i]+=1
ans=n*~-n//2
for v in d.values():
	if v>1:ans-=v*~-v//2
print(ans)