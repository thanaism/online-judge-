n=int(input())
a=list(map(int,input().split()))
t=sum(a)*0.1
a=a+a
b=[0]
for i in range(2*n):
	b.append(b[-1]+a[i])
for left in range(n):
	ok=left
	ng=left+n
	while abs(ok-ng)>1:
		mid=(ok+ng)//2
		if b[mid]-b[left]<=t:
			ok=mid
			if b[ok]-b[left)]==t:
				print('Yes')
				exit()
		else:
			ng=mid
print('No')
