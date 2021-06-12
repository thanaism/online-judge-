n=int(input())
a=[*map(int,input().split())]
"""
u: 最大値
s: sum(a[:i+1])と同等
t: 
"""
u=s=t=0
for i in range(n):
    u=max(u,a[i])
    s+=a[i]
    t+=s
    print((i+1)*u+t)