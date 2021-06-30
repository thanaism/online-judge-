a,b,c,d=map(int,input().split())
k=d*c-b
if k<=0:
	print(-1)
else:
	print(-(-a//k))