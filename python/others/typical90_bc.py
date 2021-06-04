n,p,q=map(int,input().split())
a=[*map(int,input().split())]
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                for m in range(l+1,n):
                    s=1
                    s*=a[i];s%=p
                    s*=a[j];s%=p
                    s*=a[k];s%=p
                    s*=a[l];s%=p
                    s*=a[m];s%=p
                    if s==q:ans+=1
print(ans)