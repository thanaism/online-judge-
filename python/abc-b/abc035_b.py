s=input()
t=int(input())
x=y=z=0
for c in s:
    if c=='L':x-=1
    if c=='R':x+=1
    if c=='U':y+=1
    if c=='D':y-=1
    if c=='?':
        z+=1
if t==1:
    ans=abs(x)+abs(y)+z
if t==2:
    l=abs(x)+abs(y)
    if l-z>=0:
        ans=l-z
    else:
        if (z-l)%2==0:
            ans=0
        else:
            ans=1
print(ans)

