n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]
h.sort(reverse=True)
ans=10**9
for i in range(n):
    if i+k-1<n:
        ans=min(ans,h[i]-h[i+k-1])
print(ans)