n=int(input())
a=list(map(int,input().split()))
p=[a[0]]
q=[a[-1]]
def gcd(x,y):
    if x==0:return y
    return gcd(y%x,x)
for i in range(1,n):
    p.append(gcd(p[-1],a[i]))
for i in range(n-2,-1,-1):
    q.append(gcd(q[-1],a[i]))
ans=0
for i in range(n):
    k=gcd(p[i-1],q[n-i-2])
    if i==0:k=q[-2]
    if i==n-1:k=p[-2]
    ans=max(ans,k)
print(ans)