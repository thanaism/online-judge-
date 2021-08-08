n=int(input())
a=[*map(int,input().split())]
b=sorted(a)
b=b[-2]
for i in range(n):
	if a[i]==b:
		print(i+1)