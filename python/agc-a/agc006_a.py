n=int(input())
s=input()
t=input()
for i in range(n+1):
    ok=True
    for j in range(n):
        if i+j<n and s[i+j]!=t[j]:
            ok=False
    if ok:
        print(i+n);break