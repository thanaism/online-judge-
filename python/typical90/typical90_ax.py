n,l=map(int,input().split())
MOD=10**9+7
dp=[0]*(n+1)
dp[0]=1
for i in range(n+1):
    if i+l<=n:
        dp[i+l]+=dp[i]
        dp[i+l]%=MOD
    if i+1<=n:
        dp[i+1]+=dp[i]
        dp[i+1]%=MOD
print(dp[n])
