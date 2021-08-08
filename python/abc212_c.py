input()
a=[*map(int,input().split())]
INF=1<<60
b=sorted([*map(int,input().split())]+[-INF,INF])
ans=INF
import bisect
for i in a:
	j=bisect.bisect(b,i)
	ans=min(ans,b[j]-i,i-b[j-1])
print(ans)