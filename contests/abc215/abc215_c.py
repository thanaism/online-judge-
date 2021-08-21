s,k=input().split()
k=int(k)
from itertools import permutations
ans=set()
for i in permutations(s):
	ans.add(''.join(i))
ans=sorted(list(ans))
print(ans[k-1])
