n=int(input())
a=[*map(int,input().split())]
ans=0
for i in range(1<<n):
    b=[]
    for j in range(n):
        if i>>j&1==1:
            b.append(a[j]+1)
        else:
            b.append(a[j])
    res=1
    for k in range(n):
        res*=b[k]
    if res&1==0:
        ans+=2**(bin(i).count('1'))
print(ans)
