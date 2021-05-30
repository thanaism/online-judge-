n=int(input())
s=[]
for _ in range(n):
    s.append(input())
ans=['']*n
for i in range(n):
    for j in reversed(range(n)):
        ans[i]+=s[j][i]
for i in range(n):
    print(ans[i])