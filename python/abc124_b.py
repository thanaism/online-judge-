n=int(input())
h=[*map(int,input().split())]
ans=1
top=0
for i in range(1,n):
    top=max(top,h[i-1])
    if h[i]>=top: ans+=1
print(ans)
