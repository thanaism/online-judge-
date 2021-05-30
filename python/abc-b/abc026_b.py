n=int(input())
ans=0
l=[int(input()) for _ in range(n)]
l=sorted(l,reverse=True)
from math import pi, remainder
for i in range(n):
    r=l[i]
    if i&1==0:
        ans+=r*r*pi
    else:
        ans-=r*r*pi
print(ans)