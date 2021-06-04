n,m=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
l.sort()
cnt=0
ans=0
for i in range(n):
    for j in range(l[i][1]):
        cnt+=1
        ans+=l[i][0]
        if cnt==m:
            print(ans)
            exit()
