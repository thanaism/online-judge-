from collections import deque
from heapq import heappush,heappop,heapify
n=int(input())
l=[[] for _ in range(n+1)]
# for i in range(len(l)):
	# heapify(l[i])
for _ in range(n-1):
	a,b=map(int,input().split())
	heappush(l[a],b)
	heappush(l[b],a)
# for i in range(n+1):
	# l[i].sort()
q=deque()
q.append(1)
seen=[-1]*(n+1)
seen[1]=1
ans=[]
while q:
	i=q.popleft()
	ans.append(i)
	flg=True
	# for j in l[i]:
	# 	if flg and seen[j]==-1:
	# 		seen[j]=i
	# 		q.appendleft(j)
	# 		flg=False
	# 		break
	while flg and l[i]:
		j=heappop(l[i])
		if seen[j]==-1:
			seen[j]=i
			q.appendleft(j)
			flg=False
	if flg:
		if i==1:
			print(*ans)
			exit()
		q.appendleft(seen[i])
	