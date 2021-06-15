n=int(input())
a=[*map(int,input().split())]
a.sort()
if list(range(1,n+1))==a:
	print('Yes')
else:
	print('No')