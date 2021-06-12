n,p=map(int,input().split())
a=[*map(int,input().split())]
has_odd=False
for i in a:
    if i&1==1:
        has_odd=True
        break
if has_odd:
    print(1<<(n-1))
else:
    if p==1:
        print(0)
    else:
        print(1<<n)