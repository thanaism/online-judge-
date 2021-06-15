n,q=map(int,input().split())
a=sorted([*map(int,input().split())])
INF=1<<60
a+=[INF]
d=dict()
for i,v in enumerate(a):
	d[v]=v-(i+1)
a=[0]+a
d[0]=0
for _ in range(q):
	k=int(input())
	ok=0
	ng=n+1
	while abs(ok-ng)>1:
		mid=(ok+ng)//2
		if d[a[mid]]<k:
			ok=mid
		else:
			ng=mid
	r=k-d[a[ok]]
	print(r+a[ok])
