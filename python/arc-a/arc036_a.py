n,k=map(int,input().split())
l=[]
for i in range(n):
    t=int(input())
    l.append(t)
    if len(l)>3:l=l[1:]
    if len(l)==3:
        if sum(l)<k:
            print(i+1)
            exit()
print(-1)