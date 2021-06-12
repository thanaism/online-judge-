a,b,c,k=map(int,input().split())
if k&1==0:
    ans=a-b
    if abs(ans)>10**18:ans='Unfair'
else:
    ans=b-a
    if abs(ans)>10**18:ans='Unfair'
print(ans)
