n,k=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
l.sort()
now=0
for i in range(n):
    if l[i][0]-now<=k:
        k-=l[i][0]-now
        k+=l[i][1]
        now=l[i][0]
    else:
        break
print(now+k)
