n=int(input())
ans=0
for _ in range(n):
    l=sum([*map(int,input().split())])
    if l<20: ans+=1
print(ans)

    