n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
ua=0
uc=0
for i in range(n):
    ua=max(ua,a[i])
    uc=max(uc,b[i]*ua)
    print(uc)