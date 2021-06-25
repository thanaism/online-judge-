n=int(input())
a=[*map(int,input().split())]

p=[-1]*n
def root(x):
	if p[x]<0:return x
	p[x]=root(p[x])
	return p[x]
def unite(x,y):
	rx=root(x)
	ry=root(y)
	if rx==ry:return
	if p[rx]>p[ry]:rx,ry=ry,rx
	p[rx]+=p[ry]
	p[ry]=rx
def same(x,y):
	return root(x)==root(y)

ans=0
for l in range(n):
	r=n-1-l
	if l<r:
		if not same(a[l],a[r]):
			ans+=1
			unite(a[l],a[r])

print(ans)