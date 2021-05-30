n,t=map(int,input().split())
ans=1<<60
for _ in range(n):
    cost,time=map(int,input().split())
    if time<=t: ans=min(cost,ans)
if ans==1<<60: ans='TLE'
print(ans) 
