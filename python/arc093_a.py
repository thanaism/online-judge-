n=int(input())+1
a=[0]+[*map(int,input().split())]
total=0
for i in range(n):
	total+=abs(a[i]-a[i-1])
for i in range(1,n):
	if i<n-1:
		print(
			total
			-abs(a[i]-a[i-1])
			-abs(a[i+1]-a[i])
			+abs(a[i+1]-a[i-1])
		)
	else:
		print(
			total
			-abs(a[i]-a[i-1])
			-abs(a[0]-a[i])
			+abs(a[0]-a[i-1])
		)