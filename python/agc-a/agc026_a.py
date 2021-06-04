n=int(input())
a=[*map(int,input().split())]
ans=0
for i in range(1,n):
    if a[i-1]==a[i]:
        if i+1<n:
            if a[i+1]!=a[i]-1:
                a[i]-=1
                ans+=1
            else:
                a[i]+=1
                ans+=1
        else:
            a[i]-=1
            ans+=1
print(ans)

        