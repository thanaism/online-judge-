n=int(input())
s=input()
w=[0]
e=[0]
for c in s:
	i=j=0
	if c=='W':i=1
	if c=='E':j=1
	w.append(w[-1]+i)
	e.append(e[-1]+j)
ans=1<<60
for i in range(n):
	ans=min(ans,w[i]+e[-1]-e[i+1])
print(ans)	

