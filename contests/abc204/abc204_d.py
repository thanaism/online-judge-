n=int(input())
t=[*map(int,input().split())]
s=sum(t)
"""
dp=[[False]*(s+1) for _ in range(n+1)]
dp[0][0]=True
for i in range(n):
    # for j in reversed(range(s+1)):
    for j in range(s+1):
        if j<t[i]:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=dp[i][j-t[i]]|dp[i][j]
ans=(s+1)//2
for i in range(ans,s+1):
    if dp[-1][i]:
        print(i);break
"""
dp = [False] * (s+1)
dp[0] = True
for i in range(n):
    for j in reversed(range(t[i],s+1)):
        dp[j]|=dp[j-t[i]]
ans = (s+1)//2
while not dp[ans]:
    ans+=1
print(ans)
# """