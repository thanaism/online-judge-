n,x=map(int,input().split())
m=[int(input()) for _ in range(n)]
x-=sum(m)
print(n+x//min(m))