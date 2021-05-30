n,m=map(int,input().split())
a=[input() for _ in range(n)]
b=[input() for _ in range(m)]
ans='No'
for i in range(n):
    for j in range(n):
        if i+m<=n and j+m<=n:
            ok=True
            for k in range(m):
                for l in range(m):
                    if a[i+k][j+l]!=b[k][l]:
                        ok=False
            if ok:ans='Yes'
print(ans)