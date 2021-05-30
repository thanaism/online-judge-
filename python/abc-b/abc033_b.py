n=int(input())
s,p=[],[]
for _ in range(n):
    a,b=input().split()
    s.append(a)
    p.append(int(b))
m=sum(p)
ans='atcoder'
for i in range(n):
    if p[i]*2>m:
        ans=s[i]
print(ans)