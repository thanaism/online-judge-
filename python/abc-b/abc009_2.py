n=int(input())
a=[int(input()) for _ in range(n)]
ua=max(a)
ans=0
for i in a:
    if i==ua:continue
    ans=max(ans,i)
print(ans)