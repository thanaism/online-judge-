n=int(input())
l=[[*map(int,input().split())] for _ in range(n-1)]
edges=[list() for _ in range(n+1)]
for i in range(n-1):
	a,b=l[i]
	edges[a].append(b)
	edges[b].append(a)
dp=[0]*(1<<18)

def dfs(pos,pre):
	dp[pos]=1
	for i in edges[pos]:
		if i==pre:continue
		dfs(i,pos)
		dp[pos]+=dp[i]
		print(dp[pos])

dfs(1,-1)
ans=0
for i in range(n-1):
	r=min(dp[l[i][0]],dp[l[i][1]])
	ans += r*(n-r)
print(ans)