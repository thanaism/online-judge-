h,w,n=map(int,input().split())
l=[]
rows=set()
cols=set()
for _ in range(n):
	a,b=map(int,input().split())
	l.append([a,b])
	rows.add(a)
	cols.add(b)
rows=sorted(list(rows))
cols=sorted(list(cols))
r=dict()
c=dict()
for i in range(len(rows)):
	r[rows[i]]=i+1
for i in range(len(cols)):
	c[cols[i]]=i+1
for i,j in l:
	print(r[i],c[j])
