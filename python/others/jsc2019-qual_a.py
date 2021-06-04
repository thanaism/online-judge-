m,d=map(int,input().split())
ans=0
for i in range(1,m+1):
    for j in range(1,d+1):
        if j>9:
            s=str(j)
            a=int(s[0])
            b=int(s[1])
            if a>1 and b>1 and i==a*b:
                ans+=1
print(ans)