k,t=map(int,input().split())
a=[*map(int,input().split())]
a.sort(reverse=True)
s=sum(a[1:])
print(max(a[0]-1-s,0))