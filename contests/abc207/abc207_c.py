n=int(input())
ls=[]
for _ in range(n):
	t,l,r=map(int,input().split())
	if t==2:
		r-=0.1
	if t==3:
		l+=0.1
	if t==4:
		l+=0.1
		r-=0.1
	ls.append((l,r))
ans=0
for i in range(n):
	for j in range(i+1,n):
		a,b=ls[i]
		c,d=ls[j]
		if max(a,c)<=min(b,d):ans+=1
print(ans)