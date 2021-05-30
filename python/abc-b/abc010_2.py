n=int(input())
a=[*map(int,input().split())]
ans=0
for i in a:
    if i==2:ans+=1
    if i==4:ans+=1
    if i==5:ans+=2
    if i==6:ans+=3
    if i==8:ans+=1
    if i==10:ans+=1
print(ans)