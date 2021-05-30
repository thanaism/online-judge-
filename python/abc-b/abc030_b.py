n,m=map(int,input().split())
n%=12
n*=30
n+=30*m/60
m*=6
ans=abs(n-m)
print(min(ans,360-ans))