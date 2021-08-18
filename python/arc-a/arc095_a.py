n=int(input())
x=[*map(int,input().split())]
y=sorted(x)
for i in x:
	if i<y[n//2]:
		print(y[n//2])
	else:
		print(y[n//2-1])