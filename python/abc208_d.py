n,m=map(int,input().split())
dp=[[INF:=1<<60]*n for _ in range(n)]
for i in range(n):dp[i][i]=(ans:=0)
for _ in range(m):
	a,b,c=map(int,input().split())
	dp[a-1][b-1]=c
for k in range(n):
	for i in range(n):
		for j in range(n):
			dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
			if dp[i][j]<INF:ans+=dp[i][j]		
print(ans)
