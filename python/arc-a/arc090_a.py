n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
ans=0
for i in range(n):
    ans=max(
        sum(a[:i+1])+sum(b[i:]),
        ans
    )
print(ans)