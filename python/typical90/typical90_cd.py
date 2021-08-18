l,r=input().split()
nl=len(l)
nr=len(r)
left=int(l)
r=int(r)
MOD=10**9+7
ans=0
for i in range(nl,nr+1):
	d=int('9'*i)
	right=min(r,d)
	n=right-left+1
	t=(left+right)*n//2%MOD
	t*=i
	t%=MOD
	ans+=t
	ans%=MOD
	left=right+1
print(ans)
