n=int(input())
ans=1<<60
for i in range(1,n):
    s=str(i)
    t=str(n-i)
    a=0
    for c in s:
        a+=int(c)
    b=0
    for c in t:
        b+=int(c)
    ans=min(ans,a+b)
print(ans)