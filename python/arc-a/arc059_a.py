n=int(input())
a=[*map(int,input().split())]
b=sum(a)//n
c=(sum(a)+n-1)//n
ans=min(
    sum([abs(i-b)**2 for i in a]),
    sum([abs(i-c)**2 for i in a])
)
print(ans)