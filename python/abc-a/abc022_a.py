n,s,t=map(int,input().split())
w=int(input())
ans=0
if s<=w<=t: ans+=1
for _ in range(1,n):
    w+=int(input())
    if s<=w<=t: ans+=1
print(ans)