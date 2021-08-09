n=int(input())
a=[*map(int,input().split())]

def gcd(x,y):
	if x==0:return y
	return gcd(y%x,x)

ans=a[0]
for i in range(1,n):
	ans=gcd(ans,a[i])
print(ans)