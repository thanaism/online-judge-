n=input()
ans=int(n[0])-1
ans+=9*(len(n)-1)
s=sum([int(c) for c in n])
ans=max(s,ans)
print(ans)
