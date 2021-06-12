n=int(input())
a=[*map(int,input().split())]
ans=0
for i in a:
    if i<=10:continue
    ans+=i-10
print(ans)