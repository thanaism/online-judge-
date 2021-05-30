s=input()
from itertools import groupby
ans=''
for k,g in groupby(s):
    ans+=k+str(len(list(g)))
print(ans)
