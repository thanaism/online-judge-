a,b,x,y=map(int,input().split())
d=abs(a-b)
ans=min(
    (d-1)*2*x+x if a>b else d*2*x+x,
    d*y+x if a<=b else (d-1)*y+x
)
print(ans)