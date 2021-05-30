n=int(input())
a=[*map(int,input().split())]
ave=sum(a)//n
if sum(a)!=ave*n:
    print(-1);exit()
r=0
ans=0
for i in a:
    r+=i-ave
    if r!=0:ans+=1
print(ans)