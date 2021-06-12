n=int(input())
l=list(list(map(int,input().split())) for _ in range(n))
for i in range(n):
    x=l[i][1]
    l[i][1]+=l[i][0]
    l[i][0]-=x
l.sort(key=lambda x:x[1])
now=l[0][1]
ans=1
for i in range(1,n):
    if l[i][0]>=now:
        now=l[i][1]
        ans+=1
print(ans)