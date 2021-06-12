n,m,k=map(int,input().split())
ok=False
for i in range(n+1):
    for j in range(m+1):
        if i*(m-j)+j*(n-i)==k:
            ok=True
if ok:
    print('Yes')
else:
    print('No')