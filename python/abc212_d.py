from heapq import*
h=[];d=0
for _ in range(int(input())):
	q,*x=map(int,input().split())
	if q==1:heappush(h,x[0]-d)
	elif q==2:d+=x[0]
	else:print(heappop(h)+d)
