n=int(input())
a=[*map(int,input().split())]
s=ans=sum(a)
for i in range(1,n):a[i]+=a[i-1]
for i in range(n):
    ans=min(abs(2*a[i]-s),ans)
print(ans)