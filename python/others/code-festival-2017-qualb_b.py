n=int(input())
d=[*map(int,input().split())]
m=int(input())
t=[*map(int,input().split())]
from collections import defaultdict
pos=defaultdict(int)
for i in d:
    pos[i]+=1
q=defaultdict(int)
for i in t:
    q[i]+=1
ok=True
for key in q:
    if q[key]>pos[key]:
        ok=False
if ok:
    print('YES')
else:
    print('NO')
