n=int(input())
a=[int(float(input())*(10**9)) for _ in range(n)]
def f(x,d):
    res=0
    while True:
        if x%d!=0:break
        x//=d
        res+=1
    return res
l2=[f(i,2) for i in a]
l5=[f(i,5) for i in a]
cnt=[[0]*100 for _ in range(100)]
for i in range(n):
    cnt[l2[i]][l5[i]]+=1
ans=0
for i in range(19):
    for j in range(19):
        for k in range(19):
            for l in range(19):
                if i+k<18 or j+l<18:continue
                if i==k and j==l:
                    ans+=cnt[i][j]*(cnt[k][l]-1)
                else:
                    ans+=cnt[i][j]*cnt[k][l]
ans//=2
print(ans)