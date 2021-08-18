n=int(input())
c=[*map(int,input().split())]
c.sort()
ans=c[0]
MOD=10**9+7
for i in range(1,n):
	ans*=c[i]-i
	ans%=MOD
print(ans)