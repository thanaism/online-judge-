h,w,x,y=map(int,input().split())
s=[]
for _ in range(h):
    s.append(input())
ans=0
for i in range(x,h):
    if s[i][y-1]=='#':break
    ans+=1
for i in range(x-2,-1,-1):
    if s[i][y-1]=='#':break
    ans+=1
for i in range(y,w):
    if s[x-1][i]=='#':break
    ans+=1
for i in range(y-2,-1,-1):
    if s[x-1][i]=='#':break
    ans+=1
ans+=1
print(ans)