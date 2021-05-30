n,a,b=map(int,input().split())
f=True
while n>0:
    if f:n-=a
    else:n-=b
    f=not f
if f:
    print('Bug')
else:
    print('Ant')