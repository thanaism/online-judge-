n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
c=[*map(int,input().split())]
la=[[] for _ in range(n+1)]
for i in range(n):
    la[a[i]].append(i+1)
ans=0
for i in range(n):
    ans+=len(la[b[c[i]-1]])
print(ans)