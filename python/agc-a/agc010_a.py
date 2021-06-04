n=int(input())
a=[*map(int,input().split())]
e=sum([1 for i in a if i&1==0])
o=sum([1 for i in a if i&1==1])
while e+o>2:
    e-=e//2
    if o%2==0:
        e+=o//2
        o=0
    else:
        e+=o//2
        o=1
if e+o==1 or e==2 or o==2:
    print('YES')
else:
    print('NO')