n,a,b=map(int,input().split())
c=abs(a-b)
if c&1==0:
    print(c//2)
else:
    c+=1
    print(
        min(
            min(a-1,b-1)+c//2,
            min(n-a,n-b)+c//2
        )
    )