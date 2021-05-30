_,_=map(int,input().split())
l=[*map(int,input().split())]
r=[*map(int,input().split())]
ans=0
nl=[0]*41
nr=[0]*41
for i in l:
    nl[i]+=1
for j in r:
    nr[j]+=1
for i in range(41):
    ans+=min(nl[i],nr[i])
print(ans)