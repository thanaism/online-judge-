n,m,X,Y=map(int,input().split())
x=[*map(int,input().split())]
y=[*map(int,input().split())]
ux=max(x)
ly=min(y)
flg=True
for z in range(-100,101):
    if X<z<=Y and ux<z and z<=ly:
        flg=False 
ans='No War'
if flg: ans='War'
print(ans)
