n,a,b=map(int,input().split())
ans=0
for _ in range(n):
    s,d=input().split()
    d=int(d)
    d=max(a,d)
    d=min(b,d)
    if s=='East':
        ans+=d
    else:
        ans-=d
if ans==0:
    print(0)
elif ans<0:
    print('West',-ans)
else:
    print('East',ans)