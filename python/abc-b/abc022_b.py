n=int(input())
a=[int(input()) for _ in range(n)]
s=set()
ans=0
for i in a:
    if i in s:
        ans+=1
    s.add(i)
print(ans)
    