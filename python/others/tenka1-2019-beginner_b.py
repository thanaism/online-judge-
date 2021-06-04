n=int(input())
s=input()
k=int(input())
ans=''
for c in s:
    if c!=s[k-1]:
        ans+='*'
    else:
        ans+=c
print(ans)