n=int(input())
s=[input() for _ in range(n)]
m=int(input())
t=[input() for _ in range(m)]
ans=0
for i in range(n):
    a=s.count(s[i])
    b=t.count(s[i])
    ans=max(ans,a-b)
print(ans)