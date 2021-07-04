n,k=map(int,input().split())
a=[*map(int,input().split())]
ans=k//n
b=sorted(a)
for i in a:
	if i<b[k%n]:
		print(ans+1)
	else:
		print(ans)