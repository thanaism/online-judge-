n,m=map(int,input().split())
a=[*map(int,input().split())]

def prime_factorize(x,s):
	for i in range(2,x+1):
		if i*i>x:break
		while x%i==0:
			x//=i
			s.add(i)
		if x!=1: s.add(x)
	return s

s=set()
for i in a: prime_factorize(i,s)

ans=set(range(1,m+1))
for i in s:
	if i in ans:
		j=i
		while j<=m:
			ans-={j}
			j+=i

print(len(ans))
for i in ans:
	print(i)