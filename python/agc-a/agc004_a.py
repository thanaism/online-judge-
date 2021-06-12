a,b,c=map(int,input().split())
ans=min(a*b,b*c,c*a)
if any([i&1==0 for i in [a,b,c]]):
    ans=0
print(ans)