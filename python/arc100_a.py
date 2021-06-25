n=int(input())
a=[*map(int,input().split())]
for i in range(n):
	a[i]-=i+1
a.sort()
m=n//2
if n&1:
	mid=a[m]
else:
	mid=(a[m-1]+a[m])//2
ans=0
for i in a:
	ans+=abs(i-mid)
print(ans)	