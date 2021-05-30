a,b,c,k=map(int,input().split())
s,t=map(int,input().split())
ans=s*a+t*b
if s+t>=k:ans-=c*(s+t)
print(ans)