n=int(input())
s=input()
from collections import defaultdict
d=defaultdict(int)
for c in s:
    d[c]+=1
ans=1
MOD=10**9+7
for key,val in d.items():
    ans*=val+1
    ans%=MOD
print(ans-1)