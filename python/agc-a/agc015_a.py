n,a,b=map(int,input().split())
if a>b:
    print(0)
elif a==b:
    print(1)
elif n==1:
    print(0)
else:
    l=a*(n-1)+b
    u=b*(n-1)+a
    print(u-l+1)