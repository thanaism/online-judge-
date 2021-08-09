n=int(input())
a=[*map(int,input().split())]

def gcd(x,y):
	if x==0:return y
	return gcd(y%x,x)
def lcm(x,y):
	return x*y//gcd(x,y)

d=1
for i in a: d=lcm(d,i)
ans=0
for i in a:
	ans+=(d-1)%i
print(ans)