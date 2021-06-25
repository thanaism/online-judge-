n=int(input())
l=[]
from collections import defaultdict
d=defaultdict(int)
for i in range(2,n+1):
	if i*i>n:break
	while n%i==0:
		n//=i
		d[i]+=1
if n!=1:d[n]+=1
t=sum(d.values())
x=1
ans=0
while x<t:
	x*=2
	ans+=1
print(ans)
