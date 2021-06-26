n,q=map(int,input().split())
s=input()
ls=[0]
for i in range(1,n):
	if s[i-1:i+1]=='AC':ls.append(ls[-1]+1)
	else:ls.append(ls[-1])
for _ in range(q):
	l,r=map(int,input().split())
	print(ls[r-1]-ls[l-1])

