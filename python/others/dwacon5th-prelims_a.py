n=int(input())
a=[*map(int,input().split())]
b=sum(a)/n
m=1<<60
for i in reversed(range(n)):
    if m>=abs(a[i]-b):
        m=abs(a[i]-b)
        ans=i
print(ans)
