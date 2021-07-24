n,x=map(int,input().split())
a=[*map(int,input().split())]
l=len(a[1::2])
if x>=sum(a)-l:
	print('Yes')
else:
	print('No')