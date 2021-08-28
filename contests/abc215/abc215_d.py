n,m=map(int,input().split())
a=[*map(int,input().split())]

l=110000
b=[False]*l
for i in a: b[i]=True

d=[]
for i in range(2,l):
	flg=False
	for j in range(i,l,i):
		if b[j]: flg=True
	if flg: d.append(i)

ans=set(range(1,m+1))
for i in d:
	for j in range(i,m+1,i):
		ans-={j}
		
print(len(ans))
for i in ans: print(i)