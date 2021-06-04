a,b,c=map(int,input().split())
u=max(a,b,c)
l=min(a,b,c)
m=sum([a,b,c])-u-l
ans=(u-m)+(u-l-u+m)//2
print(ans)