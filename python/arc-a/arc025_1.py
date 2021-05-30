d=[*map(int,input().split())]
j=[*map(int,input().split())]
ans=0
for i in range(7):
    ans+=max(d[i],j[i])
print(ans)