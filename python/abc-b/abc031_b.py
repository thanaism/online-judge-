l,h=map(int,input().split())
n=int(input())
for _ in range(n):
    a=int(input())
    if a>h:print(-1)
    elif l<=a<=h:print(0)
    else:print(l-a)