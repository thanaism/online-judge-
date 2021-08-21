n=int(input())
s=[ord(c)-ord('A') for c in input()]
MOD=998244353

dp = [[0]*(1<<10) for _ in range(10)]

for i in s:
	for j in range(1<<10):
		dp[i][j] *= 2
		dp[i][j] %= MOD
	for j in range(10):
		if i==j: continue
		for k in range(1<<10):
			if k>>i&1: continue
			dp[i][k^1<<i] += dp[j][k]
	dp[i][1<<i] += 1

ans = [sum(i) for i in dp]
ans = sum(ans)%MOD
print(ans)
