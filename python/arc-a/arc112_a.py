t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    d=max(0,r-2*l+1)
    ans=d*(d+1)//2
    print(ans)