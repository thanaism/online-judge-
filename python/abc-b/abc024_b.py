n,t=map(int,input().split())
prev=int(input())
ans=0
for _ in range(n-1):
    a=int(input())
    ans+=min(a-prev,t)
    prev=a
ans+=t
print(ans)