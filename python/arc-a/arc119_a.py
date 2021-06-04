n=int(input())
b=0
ans=n
while 1<<(b+1)<n:
    b+=1
    m=1<<b
    a=n//m
    c=n-a*m
    ans=min(ans,a+b+c)
print(ans)