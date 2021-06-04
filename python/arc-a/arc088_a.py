x,y=map(int,input().split())
n=x
ans=0
while n<=y:
    ans+=1
    n*=2
print(ans)