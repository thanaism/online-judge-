n,x=map(int,input().split())
x=[*map(int,input().split())]+[x]
x.sort()
d=[]
for i in range(1,len(x)):
	d.append(x[i]-x[i-1])
def gcd(x,y):
	if x==0:return y
	return gcd(y%x,x)
ans=d[0]
for i in range(1,len(d)):
	ans=gcd(ans,d[i])
print(ans)


