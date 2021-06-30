n=int(input())
a,b,c,d=[],[],[],[]
for _ in range(2):
	for _ in range(n):
		i,j=map(int,input().split())
		a.append(i)
		b.append(j)
	x=y=0
	for i in range(n):
		x+=a[i]
		y+=b[i]
		a[i]*=n
		b[i]*=n
	for i in range(n):
		a[i]-=x
		b[i]-=y
	a,c=c,a
	b,d=d,b
print(a)
print(b)
print(c)
print(d)

